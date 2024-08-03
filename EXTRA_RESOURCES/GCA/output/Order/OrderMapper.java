//WANING: this code is autogenerated with GCA by FelipedelosH
package api.crazy.demo.infraestructure.mappers;

import api.crazy.demo.domain.entities.Order;
import api.crazy.demo.infraestructure.DAO.OrderDAO.OrderEntity;

public class OrderMapper {


    public static OrderEntity toEntity(Order order) {
        return new OrderEntity(order.getId(),order.getUserId(),order.getStatus());
    }
    


    public static Order toDomain(OrderEntity order) {
        return new Order(order.getId(),order.getUserId(),order.getStatus());
    }
    

}
