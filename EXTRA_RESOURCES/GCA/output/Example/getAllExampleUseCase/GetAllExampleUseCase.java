package api.crazy.demo.domain.usecases.getAllExampleUseCase;

import java.util.List;
import api.crazy.demo.domain.entities.Example;

public abstract class GetAllExampleUseCase {
    
    public abstract List<Example> call(GetAllExampleParam param);

}