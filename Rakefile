# Faire 
# rake -T
# pour avoir un apercu des taches disponibles

desc "Compilation avec execution de pythontex"
task :compile do
  cmd = 'pdflatex main.tex && pythontex --encoding=ISO-8859-1 main.tex && pdflatex main.tex'
  execute(cmd)
end

desc "Compilation sans execution de pythontex"
task :comp do
  cmd = 'pdflatex main.tex && pdflatex main.tex'
  execute(cmd)
end


def execute(cmd)
  puts cmd
  system cmd
end
