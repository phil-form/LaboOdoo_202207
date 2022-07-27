from app.framework.injector import ContainerConfig, DependencyConfig, Scope
from app.services.comment_service import CommentService
#from app.services.auth_service import AuthService
#from app.services.auth_service_impl import AuthServiceImpl



def config_injector(config: ContainerConfig):
    #config.bind(DependencyConfig(AuthService, AuthServiceImpl, Scope.SCOPED))
    config.bind(DependencyConfig(CommentService, CommentService, Scope.SINGLETON))