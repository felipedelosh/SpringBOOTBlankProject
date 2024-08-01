package api.crazy.demo.domain.usecases.getAllExamplesUseCase;

import java.util.List;
import java.util.ArrayList;
import org.springframework.stereotype.Component;

import api.crazy.demo.domain.entities.Example;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleEntity;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleService;
//Convert database info in Java Class
import api.crazy.demo.infraestructure.mappers.ExampleMapper;

@Component //This decorator permit injection
public class GetAllExamplesUseCaseImpl extends GetAllExamplesUseCase {

    private final ExampleService exampleService;

    public GetAllExamplesUseCaseImpl(ExampleService exampleService){
        this.exampleService = exampleService;
    }

    @Override
    public List<Example> call(GetAllExamplesParam param) {

        List<Example> x = new ArrayList<>();
        List<ExampleEntity> y = exampleService.getAll();

        for (int i = 0; i < y.size(); i++) {
            x.add(ExampleMapper.toDomain(y.get(i)));
        }

        return x;
    }

}
