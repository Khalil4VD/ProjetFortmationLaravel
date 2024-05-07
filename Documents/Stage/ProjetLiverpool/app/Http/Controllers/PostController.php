<?php

namespace App\Http\Controllers;
use App\Models\Post;
use App\Models\Images;
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

        $request->validate([
            'title' => ['required', 'min:4', 'max:255', 'unique:posts'],
            'description' => ['required', 'min:15', 'max:255', 'unique:posts'],
            'Joueur' => ['required', 'image'] // Assurez-vous que le champ 'Joueur' est un fichier image
        ]);
    
        $post = new Post();
        $post->title = $request->title;
        $post->description = $request->description;
        $post->save();
    
        // Enregistrer l'image uniquement si le post est enregistré avec succès
        if ($request->hasFile('Joueur')) {
            $filename = time() . '.' . $request->file('Joueur')->getClientOriginalExtension();
    
            $path = $request->file('Joueur')->storeAs(
                'Joueurs',
                $filename,
                'public'
            );
    
            $image = new Images();
            $image->post_id = $post->id; // Utilisez l'ID du post nouvellement créé
            $image->path = $path;
            $image->save();
        }
    
        return redirect()->route('welcome');
    }
    

    public function contact(){
        return view('contact');
    }

    public function welcome(){
        return view('joueur');
    }
}
