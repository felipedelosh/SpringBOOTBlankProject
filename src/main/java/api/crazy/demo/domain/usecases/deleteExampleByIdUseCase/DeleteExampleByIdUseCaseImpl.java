package api.crazy.demo.domain.usecases.deleteExampleByIdUseCase;

import org.springframework.stereotype.Component;

import api.crazy.demo.domain.entities.Example;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleService;
import api.crazy.demo.domain.usecases.getExampleByIdUseCase.GetExampleByIdUseCase;
import api.crazy.demo.domain.usecases.getExampleByIdUseCase.GetExampleByIdUseCaseParam;
//Convert database info in Java Class
import api.crazy.demo.infraestructure.mappers.ExampleMapper;

@Component //This decorator permit injection
public class DeleteExampleByIdUseCaseImpl extends DeleteExampleByIdUseCase {

    private final ExampleService exampleservice;
    private final GetExampleByIdUseCase getExampleByIdUseCase;

    public DeleteExampleByIdUseCaseImpl(ExampleService exampleservice, GetExampleByIdUseCase getExampleByIdUseCase){
        this.exampleservice = exampleservice;
        this.getExampleByIdUseCase = getExampleByIdUseCase;
    }

    @Override
    public String call(DeleteExampleByIdUseCaseParam param) {
        try {
            Example y = getExampleByIdUseCase.call(GetExampleByIdUseCaseParam.build(param.id));
            exampleservice.deleteById(param.id);
            return "\"DELETE " + y.toString() + "\"";
        } catch (Exception e) {
            return "\"ERROR NOT FIND ELEMENT: " + e.getMessage() + "\"";
        }    
    }
    
}
