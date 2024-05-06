@extends('Layout.Liverpool')

@section('content')
<h1>Ajouter un joueur non présent sur le site</h1>

<form method="POST" action="{{ route('RouteAjout') }}">
    @csrf
    <label for="title">Nom complet du joueur:</label><br>
    <input type="text" name="title" id="title"><br><br>

    <label for="description">Description du joueur:</label><br>
    <textarea name="description" id="description" cols="60" rows="10"></textarea><br><br>

    <button type="submit">Ajouter</button>
</form>

@endsection