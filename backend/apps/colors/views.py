from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.colors.dominant_color_algorithm import DominantColorAlgorithm


class DominantColor(APIView):

    def get(self, request):
        url = request.GET.get('url')
        algorithm = DominantColorAlgorithm(url)
        rgb, dominant_color = algorithm.get_dominant_color()

        if not dominant_color:
            return Response('Unable to determine dominant color', status.HTTP_400_BAD_REQUEST)

        return Response({"rgb": rgb, "dominant_color": dominant_color})
