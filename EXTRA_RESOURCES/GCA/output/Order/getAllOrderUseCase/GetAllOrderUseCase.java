package api.crazy.demo.domain.usecases.getAllOrderUseCase;

import java.util.List;
import api.crazy.demo.domain.entities.Order;

public abstract class GetAllOrderUseCase {
    
    public abstract List<Order> call(GetAllOrderParam param);

}