from typing import List

from fastapi_pagination import paginate
from fastapi_pagination.utils import disable_installed_extensions_check
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.chmsapi.common.exception.errors import HTTPError
from src.chmsapi.models.base import generate_id
from src.chmsapi.models.member import Member
from src.chmsapi.models.department import Department
from src.chmsapi.schemas.member_schema import CreateMember, UpdateMemberSchema

disable_installed_extensions_check()
from src.chmsapi.common.logs import log


class CRUDMember:
    @staticmethod
    async def create_member(member_schema: CreateMember, db: AsyncSession) -> Member:
        log.debug("Inside create_member")
        try:
            log.debug("Creating member " + str(dict(member_schema)))
            new_member = Member(**vars(member_schema))
            department = await db.execute(select(Department).filter(Department.id == member_schema.department_id))
            new_member.id = generate_id()
            new_member.departments.append(department.scalar_one())
            db.add(new_member)
            await db.flush()
            return new_member
        except Exception as e:
            if e.__class__.__name__ == 'IntegrityError':
                log.error(e)
                raise HTTPError(code=422)
            log.error(e)
            raise HTTPError(code=422)

    @staticmethod
    async def get_all_members(db: AsyncSession) -> List[Member]:
        log.debug("Inside get_all_members")
        try:
            q = await db.execute(select(Member).order_by(Member.id))
            log.debug('Getting all members')
            return paginate(q.scalars().all())
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)

    @staticmethod
    async def get_by_id_member(db: AsyncSession, member_id: str) -> Member | None:
        log.debug("Inside get_by_id_member")
        try:
            q = await db.execute(select(Member).filter(Member.id == member_id))
            log.debug('Getting member by id ' + str(member_id))
            return q.one_or_none()
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)

    @staticmethod
    async def update_by_id_member(db: AsyncSession, member_id: str, member_schema: UpdateMemberSchema) -> Member:
        log.debug("Inside update_by_id_member")
        try:
            for var, value in vars(member_schema).items():
                setattr(member_schema, var, value) if value else None
            q = update(Member).where(Member.id == member_id).values(vars(member_schema))
            q.execution_options(synchronize_session="fetch")
            await db.execute(q)
            log.debug(f'Updating member by id {str(member_id)} with {str(vars(member_schema))}')
            return await CRUDMember.get_by_id_member(db, member_id)
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)
