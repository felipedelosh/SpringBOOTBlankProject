package api.crazy.demo.infraestructure.DAO.OrderDAO;

import java.util.List;
import org.springframework.stereotype.Service;

import lombok.AllArgsConstructor;

@Service
@AllArgsConstructor
public class OrderService {

    private final OrderRepository orderrepository;

    public List<OrderEntity> getAll(){
        var x = orderrepository.findAll();
        return x;
    }
    
}
