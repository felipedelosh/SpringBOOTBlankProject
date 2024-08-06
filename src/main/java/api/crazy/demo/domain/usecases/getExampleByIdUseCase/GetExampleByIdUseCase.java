package api.crazy.demo.domain.usecases.getExampleByIdUseCase;

import api.crazy.demo.domain.entities.Example;

public abstract class GetExampleByIdUseCase {
    
    public abstract Example call(GetExampleByIdUseCaseParam param);

}