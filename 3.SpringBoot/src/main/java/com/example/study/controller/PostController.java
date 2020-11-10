package com.example.study.controller;


import com.example.study.model.SearchParam;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class PostController {

    @PostMapping("/postMultiParameter")
    public SearchParam postMultiParameter(@RequestBody SearchParam searchParam){
        return searchParam;
    }

}
