package api.crazy.demo.infraestructure.DAO.ExampleDAO;

import java.util.List;
import org.springframework.stereotype.Service;

import lombok.AllArgsConstructor;

@Service
@AllArgsConstructor
public class ExampleService {

    private final ExampleRepository exampleRepository;

    public List<ExampleEntity> getAll(){
        var x = exampleRepository.findAll();
        return x;
    }
    
}
