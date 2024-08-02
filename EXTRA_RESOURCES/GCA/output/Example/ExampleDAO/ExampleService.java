package api.crazy.demo.infraestructure.DAO.ExampleDAO;

import java.util.List;
import org.springframework.stereotype.Service;

import lombok.AllArgsConstructor;

@Service
@AllArgsConstructor
public class ExampleService {

    private final ExampleRepository examplerepository;

    public List<ExampleEntity> getAll(){
        var x = examplerepository.findAll();
        return x;
    }
    
}
