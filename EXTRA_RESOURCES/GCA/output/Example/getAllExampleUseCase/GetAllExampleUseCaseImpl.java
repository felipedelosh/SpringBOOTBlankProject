package api.crazy.demo.domain.usecases.getAllExampleUseCase;

import java.util.List;
import java.util.ArrayList;
import org.springframework.stereotype.Component;

import api.crazy.demo.domain.entities.Example;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleEntity;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleService;
//Convert database info in Java Class
import api.crazy.demo.infraestructure.mappers.ExampleMapper;

@Component //This decorator permit injection
public class GetAllExampleUseCaseImpl extends GetAllExampleUseCase {

    private final ExampleService exampleservice;

    public GetAllExamplesUseCaseImpl(ExampleService exampleservice){
        this.exampleservice = exampleservice;
    }

    @Override
    public List<Example> call(GetAllexampleserviceParam param) {

        List<Example> x = new ArrayList<>();
        List<<ENTITYENTITY>> y = exampleservice.getAll();

        for (int i = 0; i < y.size(); i++) {
            x.add(ExampleMapper.toDomain(y.get(i)));
        }

        return x;
    }

}
