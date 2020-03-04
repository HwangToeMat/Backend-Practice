package com.HTM.vo;

public class MovieVO{
	private String movie_name; 
	private String director; 
	private String types; 
	private String moviecol; 
	private int movie_id; 
    public String getmovie_name() { return movie_name; }  
	public void setmovie_name(String movie_name) {this.movie_name = movie_name;}
    public String getdirector() { return director; }  
	public void setdirector(String director) {this.director = director;}
    public String gettypes() { return types; }  
	public void settypes(String types) {this.types = types;}
    public String getmoviecol() { return moviecol; }  
	public void setmoviecol(String moviecol) {this.moviecol = moviecol;}
    public int getmovie_id() { return movie_id; }  
	public void setmovie_id(int movie_id) {this.movie_id = movie_id;}
};