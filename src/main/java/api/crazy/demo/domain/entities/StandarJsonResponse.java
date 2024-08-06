package api.crazy.demo.domain.entities;

import java.util.Dictionary;
import java.util.Enumeration;
import java.util.Hashtable;

public class StandarJsonResponse {

    public boolean status;
    public String data;
    public String code;

    public StandarJsonResponse() {
    }

    public StandarJsonResponse(boolean status, String data, String code) {
        this.status = status;
        this.data = data;
        this.code = code;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getCodeRegister(String code) {
        Dictionary<String, String> codeDictionary = new Hashtable<>();

        codeDictionary.put("200", "OK");
        codeDictionary.put("201", "CREATE");
        codeDictionary.put("204", "EMPTY");
        codeDictionary.put("404", "NOT-FOUND");
        codeDictionary.put("500", "SERVER-ERROR");

        if (!containsKey(codeDictionary, code)) {
            return code + ":" + "CODE-SERVER-ERROR-NOT-FOUND";
        } else {
            return code + ":" + codeDictionary.get(code);
        }
    }

    public boolean containsKey(Dictionary<String, String> dict, String key) {
        Enumeration<String> keys = dict.keys();
        while (keys.hasMoreElements()) {
            if (keys.nextElement().equals(key)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public String toString() {
        String presentationStatus = "true";

        if (!this.status){
            presentationStatus = "falso";
        }

        return "{"
            + "\"status\": " + presentationStatus + "," +
            "\"data\":" + this.data + ",\n" +
            "\"code\": \"" + this.getCodeRegister(this.code) + "\"" + 
        "}";
    }

}
