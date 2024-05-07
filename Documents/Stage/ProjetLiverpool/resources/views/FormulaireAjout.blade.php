@extends('Layout.Liverpool')

@section('content')
<h1>Ajouter un joueur non présent sur le site</h1>

@if ($errors->any())
@foreach ($errors->all() as $error)
<div class="erreur" style="background-color: #C8102E; margin-left:10%; margin-right:35%; color: #FFFFFF; padding: 10px;">
    {{$error}}
</div>

@endforeach
@endif



<form method="POST" action="{{ route('RouteAjout') }}" enctype="multipart/form-data">
    @csrf
    <label for="title">Nom complet du joueur:</label><br>
    <input type="text" name="title" id="title"><br><br>

    <label for="description">Description du joueur:</label><br>
    <textarea name="description" id="description" cols="60" rows="10"></textarea><br><br>
 
    <label for="Joueur">Importez l'image de ce joueurs ci-dessous</label><br>
    <input type="file"
        id = "Joueur" name="Joueur"
        accept = "image/png, image/jpeg"><br><br>

    <button type="submit">Ajouter</button>
</form>

@endsection