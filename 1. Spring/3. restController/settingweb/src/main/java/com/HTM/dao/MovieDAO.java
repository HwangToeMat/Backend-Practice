package com.HTM.dao;
 
import java.util.List;
 
import com.HTM.vo.MovieVO;
 
public interface MovieDAO {
    
    public List<MovieVO> selectMovie() throws Exception;
}