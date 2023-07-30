from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.colors.dominant_color_algorithm import DominantColorAlgorithm


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(name='url', description='URL', type=str),
        ]
    )
)
class DominantColor(APIView):

    def get(self, request):
        url = request.GET.get('url')
        if not url:
            return Response('Invalid or missing url. Provide a valid URL', status.HTTP_400_BAD_REQUEST)

        algorithm = DominantColorAlgorithm(url)
        rgb, dominant_color, error = algorithm.get_dominant_color()

        if error:
            return Response(error, status.HTTP_400_BAD_REQUEST)

        return Response({"rgb": rgb, "dominant_color": dominant_color})
