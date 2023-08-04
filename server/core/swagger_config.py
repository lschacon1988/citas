from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view_productions = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description='''<h4>Interfaz para hacer prueba de API REST\n controla un servicio de citas y servicios según\n disponibilidad de hora y profecionales registrados</h4>''',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="lschacon1988@gmail.com"),
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny],

    url="https://server-production-citas.up.railway.app",

)

schema_view_local = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description='''<h4>Interfaz para hacer prueba de API REST\n controla un servicio de citas y servicios según\n disponibilidad de hora y profecionales registrados</h4>''',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="lschacon1988@gmail.com"),
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
