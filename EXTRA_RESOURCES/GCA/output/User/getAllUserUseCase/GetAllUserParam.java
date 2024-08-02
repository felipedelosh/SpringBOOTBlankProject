package api.crazy.demo.domain.usecases.getAllUserUseCase;

public class GetAllUserParam {

    private GetAllUserParam(){
    }

    //This is static becos not need instance... with put static you utilized without instance.
    //Only used a method
    public static GetAllUserParam build(){
        return new GetAllUserParam();
    }
    
}
