import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import './login.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TARP Chat App',
      theme: ThemeData(
        primaryColor: Colors.black,
        accentColor: Colors.white,
      ),
      home: LoginScreen(title: 'Chat App'),
      debugShowCheckedModeBanner: false,
    );
  }
}
