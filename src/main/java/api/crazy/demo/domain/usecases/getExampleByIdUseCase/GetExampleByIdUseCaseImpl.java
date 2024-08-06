package api.crazy.demo.domain.usecases.getExampleByIdUseCase;

import org.springframework.stereotype.Component;

import api.crazy.demo.domain.entities.Example;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleEntity;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleService;
//Convert database info in Java Class
import api.crazy.demo.infraestructure.mappers.ExampleMapper;

@Component //This decorator permit injection
public class GetExampleByIdUseCaseImpl extends GetExampleByIdUseCase {

    private final ExampleService exampleservice;

    public GetExampleByIdUseCaseImpl(ExampleService exampleservice){
        this.exampleservice = exampleservice;
    }

    @Override
    public Example call(GetExampleByIdUseCaseParam param) {

        ExampleEntity y = exampleservice.findById(param.id);

        return ExampleMapper.toDomain(y);
    }
    
}
