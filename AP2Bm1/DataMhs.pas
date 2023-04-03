program DataMhs;

var nama, npm, kelas:array[1..3] of string;
var i:integer;

begin
   for i := 1  to 5 do
   begin
  writeln();
  writeln('Data ke-', i);
    write ('Nama: ');
    readln(nama[i]);
    write ('NPM: ');
    readln(NPM[i]);
    write ('Kelas: ');
    readln(kelas[i]);
   end;
   
   writeln('======================');

   for i := 1  to 5 do
   begin
  writeln();
  writeln('Data ke-', i);
  writeln ('Nama: ', nama[i]);
  writeln ('NPM: ', NPM[i]);
  writeln ('Kelas: ', kelas[i]);
  end;
end.
