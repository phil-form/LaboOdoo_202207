from app.framework.injector             import ContainerConfig, DependencyConfig, Scope
from app.services.comment_service       import CommentService
from app.services.delivery_service      import DeliveryService
from app.services.message_service import MessageService
from app.services.user_service          import UserService
from app.services.service_service       import ServiceService
from app.services.service_type_service  import ServiceTypeService
from app.services.auth_service          import AuthService


def config_injector(config: ContainerConfig):
    config.bind(DependencyConfig(CommentService     , CommentService    , Scope.SINGLETON))
    config.bind(DependencyConfig(DeliveryService    , DeliveryService   , Scope.SINGLETON))
    config.bind(DependencyConfig(UserService        , UserService       , Scope.SINGLETON))
    config.bind(DependencyConfig(ServiceService     , ServiceService    , Scope.SINGLETON))
    config.bind(DependencyConfig(ServiceTypeService , ServiceTypeService, Scope.SINGLETON))
    config.bind(DependencyConfig(AuthService        , AuthService       , Scope.SINGLETON))
    config.bind(DependencyConfig(MessageService     , MessageService    , Scope.SINGLETON))
