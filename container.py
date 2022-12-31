from dependency_injector import containers, providers
from database import Database
from repositories.comment import CommentRepository
from repositories.inbody import InBodyRepository
from repositories.post import PostRepository
from repositories.user import UserRepository
from services.comment import CommentService
from services.inbody import InBodyService
from services.post import PostService
from services.user import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        "endpoints.inbody",
        "endpoints.comment",
        "endpoints.post",
        "endpoints.user",
        "endpoints.authentication",
        "common.oauth2"
    ])
    config = providers.Configuration(yaml_files=["config.yml"])
    db = providers.Singleton(Database, db_url=config.db.url)
    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )
    user_service = providers.Factory(
        UserService,
        user_repository=user_repository
    )
    post_repository = providers.Factory(
        PostRepository,
        session_factory=db.provided.session,
    )
    post_service = providers.Factory(
        PostService,
        post_repository=post_repository
    )

    comment_repository = providers.Factory(
        CommentRepository,
        session_factory=db.provided.session,
    )

    comment_service = providers.Factory(
        CommentService,
        comment_repository=comment_repository
    )

    inbody_repository = providers.Factory(
        InBodyRepository,
        session_factory=db.provided.session,
    )

    inbody_service = providers.Factory(
        InBodyService,
        inbody_repository=inbody_repository
    )
