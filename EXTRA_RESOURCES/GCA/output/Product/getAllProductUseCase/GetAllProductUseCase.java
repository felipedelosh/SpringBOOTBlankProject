package api.crazy.demo.domain.usecases.getAllProductUseCase;

import java.util.List;
import api.crazy.demo.domain.entities.Product;

public abstract class GetAllProductUseCase {
    
    public abstract List<Product> call(GetAllProductParam param);

}