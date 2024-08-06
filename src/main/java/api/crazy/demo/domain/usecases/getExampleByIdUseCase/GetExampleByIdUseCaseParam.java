package api.crazy.demo.domain.usecases.getExampleByIdUseCase;

public class GetExampleByIdUseCaseParam {

    public String id;

    private GetExampleByIdUseCaseParam(String id){
        this.id = id;
    }

    //This is static becos not need instance... with put static you utilized without instance.
    //Only used a method
    public static GetExampleByIdUseCaseParam build(String id){
        return new GetExampleByIdUseCaseParam(id);
    }
    
}
