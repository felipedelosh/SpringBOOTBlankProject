package api.crazy.demo.domain.usecases.deleteExampleByIdUseCase;

import api.crazy.demo.domain.entities.Example;

public abstract class DeleteExampleByIdUseCase {
    
    public abstract String call(DeleteExampleByIdUseCaseParam param);

}