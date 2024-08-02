package api.crazy.demo.domain.usecases.getAllProductUseCase;

import java.util.List;
import java.util.ArrayList;
import org.springframework.stereotype.Component;

import api.crazy.demo.domain.entities.Product;
import api.crazy.demo.infraestructure.DAO.ProductDAO.ProductEntity;
import api.crazy.demo.infraestructure.DAO.ProductDAO.ProductService;
//Convert database info in Java Class
import api.crazy.demo.infraestructure.mappers.ProductMapper;

@Component //This decorator permit injection
public class GetAllProductUseCaseImpl extends GetAllProductUseCase {

    private final ProductService productservice;

    public GetAllExamplesUseCaseImpl(ProductService productservice){
        this.productservice = productservice;
    }

    @Override
    public List<Product> call(GetAllproductserviceParam param) {

        List<Product> x = new ArrayList<>();
        List<<ENTITYENTITY>> y = productservice.getAll();

        for (int i = 0; i < y.size(); i++) {
            x.add(ProductMapper.toDomain(y.get(i)));
        }

        return x;
    }

}
