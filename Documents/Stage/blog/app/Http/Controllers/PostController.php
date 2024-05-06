<?php

namespace App\Http\Controllers;
use App\Models\Post;
use Illuminate\Http\Request;

class PostController extends Controller
{
    public function index(){
        $posts = Post::orderBy('title')->get();
        return view('joueur', ['posts' => $posts]);
    }

    public function show($id){
        $post = Post::findOrFail($id);
        //$posts = [
        //    1 => 'Description 1', 
         //   2 => 'Description 2'
        //];

        //$post = $posts[$id] ?? 'pas de description';

        return view('joueurs', ['post' => $post]);

    }
    
    public function create(){
        return view('FormulaireAjout');
    }

    public function ajout(Request $request){
        $post = new Post();
        $post->title = $request -> title;
        $post->description = $request -> description;
        $post->save();


    }

    public function contact(){
        return view('contact');
    }
}
