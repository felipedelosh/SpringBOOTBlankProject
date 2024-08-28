package api.crazy.demo.domain.usecases.deleteExampleByIdUseCase;

public class DeleteExampleByIdUseCaseParam {

    public String id;

    private DeleteExampleByIdUseCaseParam(String id){
        this.id = id;
    }

    //This is static becos not need instance... with put static you utilized without instance.
    //Only used a method
    public static DeleteExampleByIdUseCaseParam build(String id){
        return new DeleteExampleByIdUseCaseParam(id);
    }
    
}
