package api.crazy.demo.infraestructure.DAO.ProductDAO;

import java.util.List;
import org.springframework.stereotype.Service;

import lombok.AllArgsConstructor;

@Service
@AllArgsConstructor
public class ProductService {

    private final ProductRepository productrepository;

    public List<ProductEntity> getAll(){
        var x = productrepository.findAll();
        return x;
    }
    
}
