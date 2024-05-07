@extends('Layout.Liverpool')

@section('content')
    <h1>{{ $post->title }}</h1>
    <p>{{ $post->description }}</p>
    
    @if($post->image && $post->image->path)
        <img src="{{ Storage::url($post->image->path) }}" alt="Image du joueur">
    @else
        <p>Pas encore d'image disponible.</p>
    @endif
@endsection


