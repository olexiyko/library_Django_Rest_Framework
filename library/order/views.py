from django.shortcuts import render
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class OrderApiView(APIView):
    def get(self, request, id=None):
        if id:
            order = Order.objects.filter(pk=id).first()
            if order:
                serializer = OrderSerializer(order)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            orders = Order.objects.all()
            if orders:
                serializer = OrderSerializer(orders, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Orders not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(
                {"status": "succes", "new_order": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id:
            order = Order.objects.filter(pk=id).first()
            if order:
                order.delete()
                return Response(
                    {"success": "Order is successfuly deleted"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "Orders not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {"error": "Id id required to delete order"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def put(self, request, id=None):
        if id:
            order = Order.objects.filter(pk=id).first()
            if order:
                serializer = OrderSerializer(instance=order, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {"success": "Order is successfuly updated"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(
                {"error": "Orders not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {"error": "Id id required to update order"},
            status=status.HTTP_400_BAD_REQUEST,
        )
