desc "Compilation avec pythontex"
task :compile do
  cmd = 'pdflatex main.tex && pythontex3.py --encoding=ISO-8859-1 main.tex && pdflatex main.tex'
  execute(cmd)
end


def execute(cmd)
  puts cmd
  system cmd
end
