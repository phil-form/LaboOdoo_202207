from app.framework.injector         import ContainerConfig, DependencyConfig, Scope
from app.services.comment_service   import CommentService
from app.services.delivery_service  import DeliveryService
from app.services.user_service      import UserService
#from app.services.auth_service      import AuthService
#from app.services.auth_service_impl import AuthServiceImpl

def config_injector(config: ContainerConfig):
    config.bind(DependencyConfig(CommentService , CommentService , Scope.SINGLETON))
    config.bind(DependencyConfig(DeliveryService, DeliveryService, Scope.SINGLETON))
    config.bind(DependencyConfig(UserService    , UserService    , Scope.SINGLETON))
