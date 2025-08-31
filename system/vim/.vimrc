set nocompatible
filetype off

set number
set relativenumber
set numberwidth=4
set termguicolors
set background=dark
set cursorline
set signcolumn=yes
set colorcolumn=80
set showmatch
set laststatus=2
set showcmd
set noshowmode

set encoding=utf-8
set autoread
set hidden
set backup
set backupdir=~/.vim/backup//
set undofile
set undodir=~/.vim/undo//
set directory=~/.vim/swp//

silent! call mkdir($HOME."/.vim", "", 0770)
silent! call mkdir($HOME."/.vim/undo", "", 0700)
silent! call mkdir($HOME."/.vim/backup", "", 0700)
silent! call mkdir($HOME."/.vim/swp", "", 0700)

set autoindent
set smartindent
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set shiftround
set breakindent

set hlsearch
set incsearch
set ignorecase
set smartcase
set wrapscan

set mouse=a
set clipboard=unnamedplus
set scrolloff=8
set sidescrolloff=8
set splitbelow
set splitright
set wildmenu
set wildmode=longest:full,full
set completeopt=menu,menuone,noselect

set updatetime=150
set timeoutlen=250
set ttimeoutlen=0

set wrap
set linebreak
set textwidth=0

let data_dir = '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin('~/.vim/plugged')

Plug 'nordtheme/vim', {'branch': 'main'}
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'Yggdroot/indentLine'
Plug 'ryanoasis/vim-devicons'

Plug 'preservim/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'scrooloose/nerdcommenter'

Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'easymotion/vim-easymotion'
Plug 'haya14busa/incsearch.vim'

Plug 'tpope/vim-fugitive'
Plug 'mhinz/vim-signify'
Plug 'tpope/vim-rhubarb'

Plug 'tpope/vim-surround'
Plug 'tpope/vim-commentary'
Plug 'jiangmiao/auto-pairs'
Plug 'tpope/vim-repeat'
Plug 'mg979/vim-visual-multi'
Plug 'mattn/emmet-vim'

Plug 'neoclide/coc.nvim', {'branch': 'release'}

Plug 'pangloss/vim-javascript'
Plug 'leafgarland/typescript-vim'
Plug 'maxmellon/vim-jsx-pretty'
Plug 'othree/html5.vim'
Plug 'hail2u/vim-css3-syntax'
Plug 'cakebaker/scss-syntax.vim'
Plug 'hdima/python-syntax'
Plug 'vim-python/python-syntax'
Plug 'octol/vim-cpp-enhanced-highlight'
Plug 'bfrg/vim-cpp-modern'
Plug 'OmniSharp/omnisharp-vim'
Plug 'Shirk/vim-gas'

Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'

Plug 'liuchengxu/vim-which-key'
Plug 'mbbill/undotree'
Plug 'wesQ3/vim-windowswap'
Plug 'terryma/vim-smooth-scroll'

call plug#end()

try
    colorscheme nord
catch
    colorscheme desert
endtry

hi Normal guibg=NONE ctermbg=NONE
hi NormalNC guibg=NONE ctermbg=NONE
hi CursorLine guibg=#2E3440 ctermbg=235
hi LineNr guifg=#4C566A ctermfg=240
hi CursorLineNr guifg=#D8DEE9 gui=bold ctermfg=252 cterm=bold
hi Visual guibg=#3B4252 guifg=#D8DEE9 ctermbg=236 ctermfg=252
hi Search guibg=#3B4252 guifg=#ECEFF4 ctermbg=236 ctermfg=255
hi VertSplit guifg=#3B4252 guibg=NONE
hi StatusLine guifg=#D8DEE9 guibg=#2E3440
hi StatusLineNC guibg=#2E3440 guifg=#616E88
hi TabLine guibg=#2E3440 guifg=#81A1C1
hi TabLineFill guibg=#2E3440
hi TabLineSel guibg=NONE guifg=#88C0D0
hi ColorColumn guibg=#2E3440

hi String guifg=#8FBCBB
hi Number guifg=#81A1C1
hi Float guifg=#81A1C1
hi Boolean guifg=#88C0D0
hi Constant guifg=#88C0D0
hi Identifier guifg=#88C0D0
hi Function guifg=#5E81AC
hi Statement guifg=#81A1C1
hi Keyword guifg=#81A1C1
hi Operator guifg=#88C0D0
hi PreProc guifg=#5E81AC
hi Type guifg=#81A1C1
hi Special guifg=#8FBCBB
hi Comment guifg=#616E88
hi Error guifg=#5E81AC guibg=NONE
hi ErrorMsg guifg=#5E81AC guibg=NONE
hi WarningMsg guifg=#81A1C1 guibg=NONE
hi Todo guifg=#88C0D0 guibg=NONE
hi DiffAdd guibg=#434C5E guifg=#D8DEE9
hi DiffChange guibg=#3B4252 guifg=#D8DEE9
hi DiffDelete guibg=#2E3440 guifg=#5E81AC
hi SpellBad guifg=#5E81AC gui=undercurl
hi SpellCap guifg=#81A1C1 gui=undercurl
hi NonText guifg=#3B4252
hi SpecialKey guifg=#3B4252
hi Pmenu guibg=#2E3440 guifg=#D8DEE9
hi PmenuSel guibg=#434C5E guifg=#ECEFF4
hi SignColumn guibg=NONE
hi Title guifg=#88C0D0
hi Folded guibg=#2E3440 guifg=#616E88
hi MatchParen guibg=#434C5E guifg=#ECEFF4
hi Directory guifg=#88C0D0
hi Question guifg=#81A1C1
hi MoreMsg guifg=#81A1C1
hi ModeMsg guifg=#88C0D0

hi airline_a guibg=#2E3440 guifg=#D8DEE9
hi airline_b guibg=#3B4252 guifg=#D8DEE9
hi airline_c guibg=#434C5E guifg=#D8DEE9
hi airline_x guibg=#2E3440 guifg=#81A1C1
hi airline_y guibg=#3B4252 guifg=#81A1C1
hi airline_z guibg=#434C5E guifg=#88C0D0
hi airline_a_to_airline_b guibg=#3B4252 guifg=#2E3440
hi airline_b_to_airline_c guibg=#434C5E guifg=#3B4252
hi airline_warning guibg=#2E3440 guifg=#81A1C1
hi airline_error guibg=#2E3440 guifg=#5E81AC
hi airline_term guibg=#2E3440 guifg=#88C0D0
hi airline_c_inactive guibg=#2E3440 guifg=#616E88
hi airline_c1_inactive guibg=#2E3440 guifg=#616E88
hi airline_c2_inactive guibg=#2E3440 guifg=#616E88
hi airline_tab guibg=#2E3440 guifg=#81A1C1
hi airline_tabsel guibg=NONE guifg=#88C0D0
hi airline_tabfill guibg=#2E3440

let g:airline_theme = 'nord'
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_nr_show = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'
let g:airline#extensions#branch#enabled = 1
let g:airline#extensions#coc#enabled = 1

let g:NERDTreeWinPos = "left"
let g:NERDTreeWinSize = 35
let g:NERDTreeShowHidden = 1
let g:NERDTreeMinimalUI = 0
let g:NERDTreeAutoDeleteBuffer = 1
let g:NERDTreeQuitOnOpen = 0
let g:NERDTreeShowBookmarks = 1
let g:NERDTreeBookmarksFile = expand('~/.vim/.NERDTreeBookmarks')
let g:NERDTreeIgnore = ['\.pyc$', '\.pyo$', '\.rbc$', '\.class$', '\.o$', '\~$', '\.git$', 'node_modules']
let g:NERDTreeDirArrowExpandable = '⸸'
let g:NERDTreeDirArrowCollapsible = '⛧'
let g:NERDTreeGitStatusIndicatorMapCustom = {
    \ "Modified"  : "✦",
    \ "Staged"    : "✧",
    \ "Untracked" : "⸸",
    \ "Renamed"   : "➤",
    \ "Unmerged"  : "═",
    \ "Deleted"   : "✗",
    \ "Dirty"     : "⛧",
    \ "Clean"     : "✔",
    \ "Unknown"   : "?"
    \ }
let g:NERDTreeHighlightFolders = 1
let g:NERDTreeHighlightFoldersFullName = 1
let g:NERDTreeShowLineNumbers = 1
let g:NERDTreeChDirMode = 2

let g:fzf_layout = { 'window': { 'width': 0.9, 'height': 0.85 } }
let g:fzf_preview_window = ['right:50%:hidden', 'ctrl-/']
let g:fzf_colors = {
  \ 'fg':      ['fg', 'Normal'],
  \ 'bg':      ['bg', 'Normal'],
  \ 'hl':      ['fg', 'Comment'],
  \ 'fg+':     ['fg', 'CursorLine', 'CursorColumn', 'Normal'],
  \ 'bg+':     ['bg', 'CursorLine', 'CursorColumn'],
  \ 'hl+':     ['fg', 'Statement'],
  \ 'info':    ['fg', 'PreProc'],
  \ 'border':  ['fg', 'Ignore'],
  \ 'prompt':  ['fg', 'Conditional'],
  \ 'pointer': ['fg', 'Exception'],
  \ 'marker':  ['fg', 'Keyword'],
  \ 'spinner': ['fg', 'Label'],
  \ 'header':  ['fg', 'Comment'] }

let g:indentLine_char = '┆'
let g:indentLine_color_gui = '#2E3440'
let g:indentLine_enabled = 1
let g:indentLine_faster = 1

let g:UltiSnipsExpandTrigger = "<c-j>"
let g:UltiSnipsJumpForwardTrigger = "<c-j>"
let g:UltiSnipsJumpBackwardTrigger = "<c-k>"
let g:UltiSnipsEditSplit = "vertical"

let g:coc_global_extensions = [
  \ 'coc-json',
  \ 'coc-html',
  \ 'coc-css',
  \ 'coc-tsserver',
  \ 'coc-pyright',
  \ 'coc-clangd',
  \ 'coc-omnisharp',
  \ 'coc-emmet',
  \ 'coc-prettier',
  \ 'coc-eslint',
  \ 'coc-snippets',
  \ 'coc-pairs',
  \ 'coc-highlight'
  \ ]
let g:coc_config_home = '~/.vim'
let g:coc_data_home = '~/.vim/coc'

let g:python_highlight_all = 1
let g:python_highlight_space_errors = 0

let g:cpp_class_scope_highlight = 1
let g:cpp_member_variable_highlight = 1
let g:cpp_class_decl_highlight = 1

let g:javascript_plugin_jsdoc = 1
let g:javascript_plugin_ngdoc = 1
let g:javascript_plugin_flow = 1

let g:user_emmet_leader_key='<C-Z>'
let g:user_emmet_mode='a'

let g:which_key_timeout = 100
let g:which_key_display_names = {'<CR>': '⸸', '<TAB>': '⇶'}

let mapleader = " "
let maplocalleader = " "

nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <leader>x :qa<CR>
nnoremap <leader>c :bd<CR>

nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

nnoremap <C-Up> :resize +2<CR>
nnoremap <C-Down> :resize -2<CR>
nnoremap <C-Left> :vertical resize -2<CR>
nnoremap <C-Right> :vertical resize +2<CR>

nnoremap <Tab> :bnext<CR>
nnoremap <S-Tab> :bprev<CR>

nnoremap <leader>e :NERDTreeToggle<CR>
nnoremap <leader>f :NERDTreeFind<CR>

nnoremap <C-p> :Files<CR>
nnoremap <C-f> :Rg<CR>
nnoremap <leader>ff :Files<CR>
nnoremap <leader>fg :Rg<CR>
nnoremap <leader>fb :Buffers<CR>
nnoremap <leader>fh :History<CR>
nnoremap <leader>fc :Commands<CR>
nnoremap <leader>fl :BLines<CR>

nnoremap <leader>gs :G<CR>
nnoremap <leader>gd :Gdiff<CR>
nnoremap <leader>gl :Git log<CR>
nnoremap <leader>gb :Git blame<CR>
nnoremap <leader>gp :Git push<CR>

nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)
nmap <leader>rn <Plug>(coc-rename)
nmap <leader>f  <Plug>(coc-format-selected)
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>ca <Plug>(coc-codeaction)
nmap <leader>qf <Plug>(coc-fix-current)

nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  elseif (exists(':CocCommand') && coc#rpc#ready())
    call CocActionAsync('doHover')
  else
    execute '!' . &keywordprg . " " . expand('<cword>')
  endif
endfunction

inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

inoremap <silent><expr> <c-space> coc#refresh()
inoremap <silent><expr> <CR> pumvisible() ? coc#_select_confirm() : "\<C-g>u\<CR>"

nnoremap <leader>u :UndotreeToggle<CR>
nnoremap <leader>t :terminal<CR>
nnoremap <Esc><Esc> :nohlsearch<CR>
nnoremap <leader>/ :Commentary<CR>
vnoremap <leader>/ :Commentary<CR>

nnoremap <A-j> :m .+1<CR>==
nnoremap <A-k> :m .-2<CR>==
vnoremap <A-j> :m '>+1<CR>gv=gv
vnoremap <A-k> :m '<-2<CR>gv=gv

vnoremap < <gv
vnoremap > >gv

nnoremap n nzzzv
nnoremap N Nzzzv
nnoremap J mzJ`z
nnoremap <C-d> <C-d>zz
nnoremap <C-u> <C-u>zz

inoremap jk <ESC>

nnoremap <silent> <leader> :WhichKey '<Space>'<CR>

noremap <silent> <c-u> :call smooth_scroll#up(&scroll, 0, 2)<CR>
noremap <silent> <c-d> :call smooth_scroll#down(&scroll, 0, 2)<CR>

augroup MyAutoCommands
    autocmd!
    autocmd BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
    autocmd FileType python setlocal tabstop=4 shiftwidth=4 expandtab
    autocmd FileType javascript,typescript,html,css,json,scss setlocal tabstop=2 shiftwidth=2 expandtab
    autocmd FileType go setlocal tabstop=4 shiftwidth=4 noexpandtab
    autocmd FileType c,cpp setlocal tabstop=4 shiftwidth=4 expandtab
    autocmd FileType cs setlocal tabstop=4 shiftwidth=4 expandtab
    autocmd FileType asm setlocal tabstop=8 shiftwidth=8 noexpandtab
    autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
    autocmd VimResized * tabdo wincmd =
    autocmd BufWritePre * %s/\s\+$//e
    autocmd VimEnter * if !argc() | NERDTree | wincmd p | endif
augroup END

function! NumberToggle()
    if(&relativenumber == 1)
        set norelativenumber
    else
        set relativenumber
    endif
endfunction
nnoremap <leader>n :call NumberToggle()<CR>

command! -nargs=0 Prettier :CocCommand prettier.forceFormatDocument

filetype plugin indent on
syntax enable
