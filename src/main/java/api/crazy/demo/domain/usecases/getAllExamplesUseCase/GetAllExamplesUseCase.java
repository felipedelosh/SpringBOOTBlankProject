package api.crazy.demo.domain.usecases.getAllExamplesUseCase;

import java.util.List;
import api.crazy.demo.domain.entities.Example;

public abstract class GetAllExamplesUseCase {
    
    public abstract List<Example> call(GetAllExamplesParam param);

}
