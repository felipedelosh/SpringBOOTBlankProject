package api.crazy.demo.domain.usecases.getAllOrderUseCase;

import java.util.List;
import java.util.ArrayList;
import org.springframework.stereotype.Component;

import api.crazy.demo.domain.entities.Order;
import api.crazy.demo.infraestructure.DAO.OrderDAO.OrderEntity;
import api.crazy.demo.infraestructure.DAO.OrderDAO.OrderService;
//Convert database info in Java Class
import api.crazy.demo.infraestructure.mappers.OrderMapper;

@Component //This decorator permit injection
public class GetAllOrderUseCaseImpl extends GetAllOrderUseCase {

    private final OrderService orderservice;

    public GetAllExamplesUseCaseImpl(OrderService orderservice){
        this.orderservice = orderservice;
    }

    @Override
    public List<Order> call(GetAllorderserviceParam param) {

        List<Order> x = new ArrayList<>();
        List<<ENTITYENTITY>> y = orderservice.getAll();

        for (int i = 0; i < y.size(); i++) {
            x.add(OrderMapper.toDomain(y.get(i)));
        }

        return x;
    }

}
