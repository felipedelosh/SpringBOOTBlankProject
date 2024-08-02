package api.crazy.demo.domain.usecases.getAllExampleUseCase;

public class GetAllExampleParam {

    private GetAllExampleParam(){
    }

    //This is static becos not need instance... with put static you utilized without instance.
    //Only used a method
    public static GetAllExampleParam build(){
        return new GetAllExampleParam();
    }
    
}
