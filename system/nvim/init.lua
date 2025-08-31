local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

vim.g.mapleader = " "
vim.g.maplocalleader = " "

vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.mouse = "a"
vim.opt.showmode = false
vim.opt.clipboard = "unnamedplus"
vim.opt.breakindent = true
vim.opt.undofile = true
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.signcolumn = "yes"
vim.opt.updatetime = 200
vim.opt.timeoutlen = 300
vim.opt.splitright = true
vim.opt.splitbelow = true
vim.opt.inccommand = "split"
vim.opt.cursorline = true
vim.opt.scrolloff = 12
vim.opt.tabstop = 2
vim.opt.shiftwidth = 2
vim.opt.expandtab = true
vim.opt.termguicolors = true
vim.opt.background = "dark"

require("lazy").setup({
  {
    "catppuccin/nvim",
    name = "catppuccin",
    priority = 1000,
    config = function()
      require("catppuccin").setup({
        flavour = "mocha",
        background = {
          light = "latte",
          dark = "mocha",
        },
        transparent_background = false,
        show_end_of_buffer = false,
        term_colors = true,
        dim_inactive = {
          enabled = true,
          shade = "dark",
          percentage = 0.2,
        },
        no_italic = false,
        no_bold = false,
        no_underline = false,
        styles = {
          comments = { "italic" },
          conditionals = { "italic" },
          loops = {},
          functions = { "bold" },
          keywords = { "italic", "bold" },
          strings = {},
          variables = {},
          numbers = {},
          booleans = { "italic" },
          properties = {},
          types = { "italic" },
          operators = {},
        },
        color_overrides = {
          mocha = {
            base = "#0e0e15",
            mantle = "#14141f",
            surface0 = "#252535",
            surface1 = "#35354a",
            surface2 = "#4a4a60",
            overlay0 = "#606070",
            overlay1 = "#75758a",
            overlay2 = "#8a8aa0",
            subtext0 = "#a0a0b8",
            subtext1 = "#b8b8d0",
            text = "#d0d0e8",
            lavender = "#a3a3e0",
            blue = "#7a7af5",
            sapphire = "#5a8ac8",
            sky = "#70a0d0",
            teal = "#80c0b8",
            green = "#90c090",
            yellow = "#e0c080",
            peach = "#e8a070",
            maroon = "#d08090",
            red = "#e07080",
            mauve = "#b090d8",
            pink = "#d8a0c0",
            flamingo = "#e0b0b8",
            rosewater = "#e8c0c0",
          },
        },
        custom_highlights = function(colors)
          return {
            CursorLine = { bg = colors.surface0 },
            LineNr = { fg = colors.overlay0 },
            CursorLineNr = { fg = colors.mauve, style = { "bold" } },
            Visual = { bg = colors.surface1, fg = colors.text },
            IncSearch = { bg = colors.peach, fg = colors.base, style = { "bold" } },
            Search = { bg = colors.surface2, fg = colors.text },
            NvimTreeNormal = { bg = colors.mantle },
            NvimTreeEndOfBuffer = { bg = colors.mantle },
            NvimTreeWinSeparator = { fg = colors.surface0, bg = colors.mantle },
            BufferLineFill = { bg = colors.mantle },
            BufferLineBackground = { fg = colors.subtext0, bg = colors.surface0 },
            BufferLineBufferSelected = { fg = colors.text, bg = colors.base, style = { "bold" } },
            BufferLineIndicatorSelected = { fg = colors.mauve, bg = colors.base },
            BufferLineSeparator = { fg = colors.mantle, bg = colors.surface0 },
            BufferLineSeparatorSelected = { fg = colors.mantle, bg = colors.base },
            Pmenu = { bg = colors.mantle, fg = colors.text },
            PmenuSel = { bg = colors.surface1, fg = colors.mauve },
            NormalFloat = { bg = colors.mantle },
            FloatBorder = { fg = colors.overlay0, bg = colors.mantle },
            TelescopeBorder = { fg = colors.overlay0, bg = colors.mantle },
            TelescopePromptBorder = { fg = colors.overlay1, bg = colors.mantle },
            TelescopeResultsBorder = { fg = colors.overlay0, bg = colors.mantle },
            TelescopePreviewBorder = { fg = colors.overlay0, bg = colors.mantle },
            TelescopeSelection = { bg = colors.surface1, fg = colors.mauve },
            WhichKeyFloat = { bg = colors.mantle },
          }
        end,
        integrations = {
          cmp = true,
          gitsigns = true,
          nvimtree = true,
          treesitter = true,
          notify = true,
          telescope = {
            enabled = true,
            style = "nvchad",
          },
          lsp_trouble = false,
          which_key = true,
          indent_blankline = {
            enabled = true,
            colored_indent_levels = true,
          },
          noice = true,
        },
      })
      vim.cmd.colorscheme("catppuccin")
    end,
  },

  {
    "nvim-tree/nvim-tree.lua",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      vim.g.loaded_netrw = 1
      vim.g.loaded_netrwPlugin = 1
      
      require("nvim-tree").setup({
        auto_reload_on_write = true,
        disable_netrw = true,
        hijack_netrw = true,
        hijack_cursor = false,
        hijack_unnamed_buffer_when_opening = false,
        sort = {
          sorter = "case_sensitive",
        },
        view = {
          centralize_selection = true,
          cursorline = true,
          debounce_delay = 15,
          width = 35,
          side = "left",
          preserve_window_proportions = false,
          number = false,
          relativenumber = false,
          signcolumn = "yes",
        },
        renderer = {
          add_trailing = false,
          group_empty = true,
          highlight_git = "name",
          full_name = false,
          highlight_opened_files = "name",
          highlight_modified = "name",
          root_folder_label = ":~:s?$?/..?",
          indent_width = 2,
          indent_markers = {
            enable = true,
            inline_arrows = true,
            icons = {
              corner = "└",
              edge = "│",
              item = "│",
              bottom = "─",
              none = " ",
            },
          },
          icons = {
            webdev_colors = true,
            git_placement = "before",
            modified_placement = "after",
            padding = " ",
            symlink_arrow = " ➛ ",
            show = {
              file = true,
              folder = true,
              folder_arrow = true,
              git = true,
              modified = true,
            },
            glyphs = {
              default = "☠︎︎",
              symlink = "🔗",
              bookmark = "🔖",
              modified = "⛧",
              folder = {
                arrow_closed = "▶",
                arrow_open = "▼",
                default = "༺𓆩☠︎︎𓆪༻",
                open = "熱",
                empty = "𓆩♱𓆪",
                empty_open = "⋆𖤍⋆",
                symlink = "𓆩☠︎︎𓆪",
                symlink_open = "⛧ᶻ𝗓𐰁",
              },
              git = {
                unstaged = "𓆩✗𓆪",
                staged = "𓆩✓𓆪",
                unmerged = "𓆩↯𓆪",
                renamed = "𓆩➜𓆪",
                untracked = "𓆩★𓆪",
                deleted = "𓆩🗑𓆪",
                ignored = "𓆩◌𓆪",
              },
            },
          },
          special_files = { "Cargo.toml", "Makefile", "README.md", "readme.md", "package.json" },
          symlink_destination = true,
        },
        hijack_directories = {
          enable = true,
          auto_open = true,
        },
        update_focused_file = {
          enable = true,
          update_root = {
            enable = false,
            ignore_list = {},
          },
          exclude = false,
        },
        filters = {
          enable = true,
          git_ignored = true,
          dotfiles = false,
          git_clean = false,
          no_buffer = false,
          custom = {},
          exclude = {},
        },
        filesystem_watchers = {
          enable = true,
          debounce_delay = 50,
          ignore_dirs = {},
        },
        git = {
          enable = true,
          show_on_dirs = true,
          show_on_open_dirs = true,
          disable_for_dirs = {},
          timeout = 400,
        },
        modified = {
          enable = true,
          show_on_dirs = true,
          show_on_open_dirs = true,
        },
        actions = {
          use_system_clipboard = true,
          change_dir = {
            enable = true,
            global = false,
            restrict_above_cwd = false,
          },
          expand_all = {
            max_folder_discovery = 300,
            exclude = {},
          },
          file_popup = {
            open_win_config = {
              col = 1,
              row = 1,
              relative = "cursor",
              border = "shadow",
              style = "minimal",
            },
          },
          open_file = {
            quit_on_open = false,
            eject = true,
            resize_window = true,
            window_picker = {
              enable = true,
              picker = "default",
              chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
              exclude = {
                filetype = { "notify", "packer", "qf", "diff", "fugitive", "fugitiveblame" },
                buftype = { "nofile", "terminal", "help" },
              },
            },
          },
          remove_file = {
            close_window = true,
          },
        },
        trash = {
          cmd = "gio trash",
        },
        live_filter = {
          prefix = "[FILTER]: ",
          always_show_folders = true,
        },
        tab = {
          sync = {
            open = false,
            close = false,
            ignore = {},
          },
        },
        notify = {
          threshold = vim.log.levels.INFO,
          absolute_path = true,
        },
        help = {
          sort_by = "key",
        },
        ui = {
          confirm = {
            remove = true,
            trash = true,
            default_yes = false,
          },
        },
        experimental = {},
        log = {
          enable = false,
          truncate = false,
          types = {
            all = false,
            config = false,
            copy_paste = false,
            dev = false,
            diagnostics = false,
            git = false,
            profile = false,
            watcher = false,
          },
        },
        system_open = {
          cmd = "",
          args = {},
        },
      })

      vim.api.nvim_create_autocmd("VimEnter", {
        callback = function()
          if vim.fn.argc() == 0 then
            vim.schedule(function()
              require("nvim-tree.api").tree.open()
            end)
          end
        end,
      })
    end,
  },

  {
    "nvim-lualine/lualine.nvim",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      require("lualine").setup({
        options = {
          theme = "catppuccin",
          component_separators = { left = "│", right = "│" },
          section_separators = { left = "", right = "" },
          disabled_filetypes = {
            statusline = {},
            winbar = {},
          },
          ignore_focus = {},
          always_divide_middle = true,
          globalstatus = true,
          refresh = {
            statusline = 1000,
            tabline = 1000,
            winbar = 1000,
          },
        },
        sections = {
          lualine_a = {
            { "mode", separator = { left = "" }, right_padding = 2 },
          },
          lualine_b = {
            "branch",
            {
              "diff",
              colored = true,
              diff_color = {
                added = { fg = "#90c090" },
                modified = { fg = "#e0c080" },
                removed = { fg = "#e07080" },
              },
              symbols = { added = "𓆩𓆪 ", modified = "𓆩柳𓆪", removed = "𓆩𓆪 " },
            },
          },
          lualine_c = {
            {
              "filename",
              file_status = true,
              newfile_status = true,
              path = 1,
              shorting_target = 40,
              symbols = {
                modified = "𖤐",
                readonly = "ᵎ!ᵎ",
                unnamed = "[No Name]",
                newfile = "[New]",
              },
            },
          },
          lualine_x = {
            {
              "diagnostics",
              sources = { "nvim_diagnostic", "nvim_lsp" },
              sections = { "error", "warn", "info", "hint" },
              diagnostics_color = {
                error = { fg = "#e07080" },
                warn = { fg = "#e0c080" },
                info = { fg = "#7a7af5" },
                hint = { fg = "#80c0b8" },
              },
              symbols = { error = "𓆩✘𓆪 ", warn = "𓆩▲𓆪 ", info = "𓆩ℹ𓆪 ", hint = "𓆩➤𓆪 " },
              colored = true,
              update_in_insert = false,
              always_visible = false,
            },
            "encoding",
            "fileformat",
            "filetype",
          },
          lualine_y = { "progress" },
          lualine_z = {
            { "location", separator = { right = "" }, left_padding = 2 },
          },
        },
        inactive_sections = {
          lualine_a = {},
          lualine_b = {},
          lualine_c = { "filename" },
          lualine_x = { "location" },
          lualine_y = {},
          lualine_z = {},
        },
        tabline = {},
        winbar = {},
        inactive_winbar = {},
        extensions = { "nvim-tree", "lazy" },
      })
    end,
  },

  {
    "akinsho/bufferline.nvim",
    version = "*",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      require("bufferline").setup({
        options = {
          mode = "buffers",
          style_preset = require("bufferline").style_preset.default,
          themable = true,
          numbers = "ordinal",
          close_command = "bdelete! %d",
          right_mouse_command = "bdelete! %d",
          left_mouse_command = "buffer %d",
          middle_mouse_command = nil,
          indicator = {
            icon = "▊",
            style = "icon",
          },
          buffer_close_icon = "𓆩✖𓆪",
          modified_icon = "𖤐",
          close_icon = "",
          left_trunc_marker = "◄",
          right_trunc_marker = "►",
          max_name_length = 30,
          max_prefix_length = 30,
          truncate_names = true,
          tab_size = 21,
          diagnostics = "nvim_lsp",
          diagnostics_update_in_insert = false,
          diagnostics_indicator = function(count, level)
            local icon = level:match("error") and "𓆩✘𓆪" or level:match("warning") and "𓆩▲𓆪" or "𓆩➤𓆪"
            return " " .. icon .. count
          end,
          color_icons = true,
          get_element_icon = function(element)
            local icon, hl = require("nvim-web-devicons").get_icon_by_filetype(element.filetype, { default = false })
            return icon, hl
          end,
          show_buffer_icons = true,
          show_buffer_close_icons = true,
          show_close_icon = true,
          show_tab_indicators = true,
          show_duplicate_prefix = true,
          duplicates_across_groups = true,
          persist_buffer_sort = true,
          move_wraps_at_ends = false,
          separator_style = "thin",
          enforce_regular_tabs = false,
          always_show_bufferline = true,
          auto_toggle_bufferline = true,
          hover = {
            enabled = true,
            delay = 150,
            reveal = { "close" },
          },
          sort_by = "insert_after_current",
          offsets = {
            {
              filetype = "NvimTree",
              text = "‿̩͙⊱༒︎༻（ ͜.人 ͜.）Bitch!愛⛧",
              text_align = "center",
              separator = true,
              highlight = "Directory",
            },
          },
          custom_areas = {
            right = function()
              local result = {}
              local seve = vim.diagnostic.severity
              local error = #vim.diagnostic.get(0, { severity = seve.ERROR })
              local warning = #vim.diagnostic.get(0, { severity = seve.WARN })
              local info = #vim.diagnostic.get(0, { severity = seve.INFO })
              local hint = #vim.diagnostic.get(0, { severity = seve.HINT })

              if error ~= 0 then
                table.insert(result, { text = " 𓆩✘𓆪" .. error, link = "DiagnosticError" })
              end
              if warning ~= 0 then
                table.insert(result, { text = " 𓆩▲𓆪" .. warning, link = "DiagnosticWarn" })
              end
              if hint ~= 0 then
                table.insert(result, { text = " 𓆩➤𓆪" .. hint, link = "DiagnosticHint" })
              end
              if info ~= 0 then
                table.insert(result, { text = " 𓆩ℹ𓆪" .. info, link = "DiagnosticInfo" })
              end
              return result
            end,
          },
        },
      })
    end,
  },

  {
    "nvim-telescope/telescope.nvim",
    tag = "0.1.8",
    dependencies = {
      "nvim-lua/plenary.nvim",
      { "nvim-telescope/telescope-fzf-native.nvim", build = "make" },
      "nvim-telescope/telescope-ui-select.nvim",
    },
    config = function()
      require("telescope").setup({
        defaults = {
          prompt_prefix = "𓆩🔍𓆪 ",
          selection_caret = "𓆩➤𓆪 ",
          path_display = { "truncate" },
          winblend = 10,
          layout_strategy = "horizontal",
          layout_config = {
            horizontal = {
              prompt_position = "top",
              preview_width = 0.55,
              results_width = 0.8,
            },
            vertical = {
              mirror = false,
            },
            width = 0.9,
            height = 0.85,
            preview_cutoff = 120,
          },
          sorting_strategy = "ascending",
          mappings = {
            i = {
              ["<C-n>"] = "move_selection_next",
              ["<C-p>"] = "move_selection_previous",
              ["<C-c>"] = "close",
              ["<Down>"] = "move_selection_next",
              ["<Up>"] = "move_selection_previous",
              ["<CR>"] = "select_default",
              ["<C-x>"] = "select_horizontal",
              ["<C-v>"] = "select_vertical",
              ["<C-t>"] = "select_tab",
              ["<C-u>"] = "preview_scrolling_up",
              ["<C-d>"] = "preview_scrolling_down",
              ["<PageUp>"] = "results_scrolling_up",
              ["<PageDown>"] = "results_scrolling_down",
              ["<Tab>"] = "toggle_selection",
              ["<S-Tab>"] = "toggle_selection",
              ["<C-q>"] = "send_to_qflist",
              ["<M-q>"] = "send_selected_to_qflist",
              ["<C-l>"] = "complete_tag",
              ["<C-/>"] = "which_key",
            },
            n = {
              ["<esc>"] = "close",
              ["<CR>"] = "select_default",
              ["<C-x>"] = "select_horizontal",
              ["<C-v>"] = "select_vertical",
              ["<C-t>"] = "select_tab",
              ["<Tab>"] = "toggle_selection",
              ["<S-Tab>"] = "toggle_selection",
              ["<C-q>"] = "send_to_qflist",
              ["<M-q>"] = "send_selected_to_qflist",
              ["j"] = "move_selection_next",
              ["k"] = "move_selection_previous",
              ["H"] = "move_to_top",
              ["M"] = "move_to_middle",
              ["L"] = "move_to_bottom",
              ["<Down>"] = "move_selection_next",
              ["<Up>"] = "move_selection_previous",
              ["gg"] = "move_to_top",
              ["G"] = "move_to_bottom",
              ["<C-u>"] = "preview_scrolling_up",
              ["<C-d>"] = "preview_scrolling_down",
              ["<PageUp>"] = "results_scrolling_up",
              ["<PageDown>"] = "results_scrolling_down",
              ["?"] = "which_key",
            },
          },
          borderchars = { "─", "│", "─", "│", "┌", "┐", "┘", "└" },
          color_devicons = true,
          use_less = true,
          set_env = { ["COLORTERM"] = "truecolor" },
          file_previewer = require("telescope.previewers").vim_buffer_cat.new,
          grep_previewer = require("telescope.previewers").vim_buffer_vimgrep.new,
          qflist_previewer = require("telescope.previewers").vim_buffer_qflist.new,
          buffer_previewer_maker = require("telescope.previewers").buffer_previewer_maker,
        },
        pickers = {
          find_files = {
            theme = "dropdown",
            previewer = false,
          },
          live_grep = {
            theme = "ivy",
          },
          buffers = {
            theme = "dropdown",
            previewer = false,
            initial_mode = "normal",
            mappings = {
              i = {
                ["<C-d>"] = "delete_buffer",
              },
              n = {
                ["dd"] = "delete_buffer",
              },
            },
          },
        },
        extensions = {
          fzf = {
            fuzzy = true,
            override_generic_sorter = true,
            override_file_sorter = true,
            case_mode = "smart_case",
          },
          ["ui-select"] = {
            require("telescope.themes").get_dropdown({}),
          },
        },
      })
      
      require("telescope").load_extension("fzf")
      require("telescope").load_extension("ui-select")
    end,
  },

  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    dependencies = {
      "nvim-treesitter/nvim-treesitter-textobjects",
      "nvim-treesitter/nvim-treesitter-context",
      "windwp/nvim-ts-autotag",
    },
    config = function()
      require("nvim-treesitter.configs").setup({
        ensure_installed = {
          "lua",
          "luadoc",
          "javascript",
          "typescript",
          "tsx",
          "html",
          "css",
          "scss",
          "json",
          "markdown",
          "markdown_inline",
          "java",
          "python",
          "bash",
          "yaml",
          "toml",
          "vim",
          "vimdoc",
          "regex",
          "diff",
          "git_config",
          "git_rebase",
          "gitcommit",
          "gitignore",
        },
        sync_install = false,
        auto_install = true,
        ignore_install = {},
        modules = {},
        highlight = {
          enable = true,
          disable = function(lang, buf)
            local max_filesize = 100 * 1024 -- 100 KB
            local ok, stats = pcall(vim.loop.fs_stat, vim.api.nvim_buf_get_name(buf))
            if ok and stats and stats.size > max_filesize then
              return true
            end
          end,
          additional_vim_regex_highlighting = false,
        },
        indent = {
          enable = true,
          disable = { "python" },
        },
        autotag = {
          enable = true,
        },
        incremental_selection = {
          enable = true,
          keymaps = {
            init_selection = "<C-space>",
            node_incremental = "<C-space>",
            scope_incremental = false,
            node_decremental = "<bs>",
          },
        },
        textobjects = {
          select = {
            enable = true,
            lookahead = true,
            keymaps = {
              ["aa"] = "@parameter.outer",
              ["ia"] = "@parameter.inner",
              ["af"] = "@function.outer",
              ["if"] = "@function.inner",
              ["ac"] = "@class.outer",
              ["ic"] = "@class.inner",
              ["ii"] = "@conditional.inner",
              ["ai"] = "@conditional.outer",
              ["il"] = "@loop.inner",
              ["al"] = "@loop.outer",
            },
          },
          move = {
            enable = true,
            set_jumps = true,
            goto_next_start = {
              ["]m"] = "@function.outer",
              ["]]"] = "@class.outer",
              ["]o"] = "@loop.*",
              ["]s"] = { query = "@scope", query_group = "locals", desc = "Next scope" },
              ["]z"] = { query = "@fold", query_group = "folds", desc = "Next fold" },
            },
            goto_next_end = {
              ["]M"] = "@function.outer",
              ["]["] = "@class.outer",
            },
            goto_previous_start = {
              ["[m"] = "@function.outer",
              ["[["] = "@class.outer",
            },
            goto_previous_end = {
              ["[M"] = "@function.outer",
              ["[]"] = "@class.outer",
            },
          },
        },
      })
      
      require("treesitter-context").setup({
        enable = true,
        max_lines = 0,
        min_window_height = 0,
        line_numbers = true,
        multiline_threshold = 20,
        trim_scope = "outer",
        mode = "cursor",
        separator = "─",
        zindex = 20,
        on_attach = nil,
      })
    end,
  },

  {
    "hrsh7th/nvim-cmp",
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-buffer",
      "hrsh7th/cmp-path",
      "hrsh7th/cmp-cmdline",
      "L3MON4D3/LuaSnip",
      "saadparwaiz1/cmp_luasnip",
      "onsails/lspkind.nvim",
      "rafamadriz/friendly-snippets",
    },
    config = function()
      local cmp = require("cmp")
      local luasnip = require("luasnip")
      local lspkind = require("lspkind")

      require("luasnip.loaders.from_vscode").lazy_load()

      cmp.setup({
        snippet = {
          expand = function(args)
            luasnip.lsp_expand(args.body)
          end,
        },
        window = {
          completion = {
            border = { "┌", "─", "┐", "│", "┘", "─", "└", "│" },
            winhighlight = "Normal:CmpPmenu,FloatBorder:CmpPmenuBorder,CursorLine:PmenuSel,Search:None",
            scrolloff = 0,
            col_offset = 0,
            side_padding = 1,
          },
          documentation = {
            border = { "┌", "─", "┐", "│", "┘", "─", "└", "│" },
            winhighlight = "Normal:CmpDoc,FloatBorder:CmpDocBorder",
            max_width = 120,
            min_width = 60,
            max_height = math.floor(0.3 * vim.o.lines),
            min_height = 1,
          },
        },
        formatting = {
          fields = { "kind", "abbr", "menu" },
          format = lspkind.cmp_format({
            mode = "symbol_text",
            maxwidth = 50,
            ellipsis_char = "…",
            show_labelDetails = true,
            before = function(entry, vim_item)
              vim_item.menu = ({
                nvim_lsp = "[LSP]",
                luasnip = "[Snippet]",
                buffer = "[Buffer]",
                path = "[Path]",
              })[entry.source.name]
              return vim_item
            end,
          }),
        },
        mapping = cmp.mapping.preset.insert({
          ["<C-b>"] = cmp.mapping.scroll_docs(-4),
          ["<C-f>"] = cmp.mapping.scroll_docs(4),
          ["<C-Space>"] = cmp.mapping.complete(),
          ["<C-e>"] = cmp.mapping.abort(),
          ["<CR>"] = cmp.mapping.confirm({
            behavior = cmp.ConfirmBehavior.Replace,
            select = true,
          }),
          ["<Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_next_item()
            elseif luasnip.expand_or_locally_jumpable() then
              luasnip.expand_or_jump()
            else
              fallback()
            end
          end, { "i", "s" }),
          ["<S-Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_prev_item()
            elseif luasnip.locally_jumpable(-1) then
              luasnip.jump(-1)
            else
              fallback()
            end
          end, { "i", "s" }),
        }),
        sources = cmp.config.sources({
          { name = "nvim_lsp", priority = 1000 },
          { name = "luasnip", priority = 750 },
        }, {
          { name = "buffer", priority = 500 },
          { name = "path", priority = 250 },
        }),
        experimental = {
          ghost_text = true,
        },
      })

      cmp.setup.cmdline({ "/", "?" }, {
        mapping = cmp.mapping.preset.cmdline(),
        sources = {
          { name = "buffer" },
        },
      })

      cmp.setup.cmdline(":", {
        mapping = cmp.mapping.preset.cmdline(),
        sources = cmp.config.sources({
          { name = "path" },
        }, {
          { name = "cmdline" },
        }),
        matching = { disallow_symbol_nonprefix_matching = false },
      })
    end,
  },

  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
      "j-hui/fidget.nvim",
      "folke/neodev.nvim",
    },
    config = function()
      require("neodev").setup()
      require("fidget").setup({
        progress = {
          poll_rate = 0,
          suppress_on_insert = false,
          ignore_done_already = false,
          ignore_empty_message = false,
          clear_on_detach = function(client_id)
            local client = vim.lsp.get_client_by_id(client_id)
            return client and client.name or nil
          end,
          notification_group = function(msg)
            return msg.lsp_client.name
          end,
          ignore = {},
          lsp = {
            progress_ringbuf_size = 0,
          },
          display = {
            render_limit = 16,
            done_ttl = 3,
            done_icon = "𓆩✔𓆪",
            done_style = "Constant",
            progress_ttl = math.huge,
            progress_icon = { pattern = "moon", period = 1 },
            progress_style = "WarningMsg",
            group_style = "Title",
            icon_style = "Question",
            priority = 30,
            skip_history = true,
            format_message = require("fidget.progress.display").default_format_message,
            format_annote = function(msg)
              return msg.title
            end,
            format_group_name = function(group)
              return tostring(group)
            end,
            overrides = {
              rust_analyzer = { name = "rust-analyzer" },
            },
          },
        },
        notification = {
          poll_rate = 10,
          filter = vim.log.levels.INFO,
          history_size = 128,
          override_vim_notify = true,
          configs = { default = require("fidget.notification").default_config },
          redirect = function(msg, level, opts)
            if opts and opts.on_open then
              return require("fidget.integration.nvim-notify").delegate(msg, level, opts)
            end
          end,
          view = {
            stack_upwards = true,
            icon_separator = " ",
            group_separator = "───",
            group_separator_hl = "Comment",
            render_message = function(msg, cnt)
              return cnt == 1 and msg or string.format("(%dx) %s", cnt, msg)
            end,
          },
          window = {
            normal_hl = "Comment",
            winblend = 0,
            border = "rounded",
            zindex = 45,
            max_width = 0,
            max_height = 0,
            x_padding = 1,
            y_padding = 1,
            align = "bottom",
            relative = "editor",
          },
        },
        integration = {
          ["nvim-tree"] = {
            enable = true,
          },
        },
        logger = {
          level = vim.log.levels.WARN,
          max_size = 10000,
          float_precision = 0.01,
          path = string.format("%s/fidget.nvim.log", vim.fn.stdpath("cache")),
        },
      })

      require("mason").setup({
        ui = {
          border = "rounded",
          width = 0.8,
          height = 0.9,
          icons = {
            package_installed = "𓆩✓𓆪",
            package_pending = "𓆩➜𓆪",
            package_uninstalled = "𓆩✗𓆪",
          },
        },
      })

      require("mason-lspconfig").setup({
        ensure_installed = {
          "lua_ls",
          "ts_ls",
          "html",
          "cssls",
          "eslint",
          "jsonls",
          "jdtls",
          "pylsp",
          "bashls",
        },
        automatic_installation = true,
      })

      local lspconfig = require("lspconfig")
      local capabilities = require("cmp_nvim_lsp").default_capabilities()

      capabilities.textDocument.completion.completionItem = {
        documentationFormat = { "markdown", "plaintext" },
        snippetSupport = true,
        preselectSupport = true,
        insertReplaceSupport = true,
        labelDetailsSupport = true,
        deprecatedSupport = true,
        commitCharactersSupport = true,
        tagSupport = { valueSet = { 1 } },
        resolveSupport = {
          properties = {
            "documentation",
            "detail",
            "additionalTextEdits",
          },
        },
      }

      local on_attach = function(client, bufnr)
        local opts = { buffer = bufnr, silent = true }

        vim.keymap.set("n", "gd", vim.lsp.buf.definition, opts)
        vim.keymap.set("n", "gD", vim.lsp.buf.declaration, opts)
        vim.keymap.set("n", "gi", vim.lsp.buf.implementation, opts)
        vim.keymap.set("n", "gr", vim.lsp.buf.references, opts)
        vim.keymap.set("n", "K", vim.lsp.buf.hover, opts)
        vim.keymap.set("n", "<C-k>", vim.lsp.buf.signature_help, opts)
        vim.keymap.set("n", "<space>rn", vim.lsp.buf.rename, opts)
        vim.keymap.set("n", "<space>ca", vim.lsp.buf.code_action, opts)
        vim.keymap.set("n", "<space>f", function()
          vim.lsp.buf.format { async = true }
        end, opts)

        if client.supports_method("textDocument/inlayHint") then
          vim.lsp.inlay_hint.enable(true, { bufnr = bufnr })
        end
      end

      lspconfig.lua_ls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        settings = {
          Lua = {
            runtime = {
              version = "LuaJIT",
            },
            diagnostics = {
              globals = { "vim" },
              disable = { "missing-fields" },
            },
            workspace = {
              library = vim.api.nvim_get_runtime_file("", true),
              checkThirdParty = false,
            },
            telemetry = {
              enable = false,
            },
            format = {
              enable = true,
              defaultConfig = {
                indent_style = "space",
                indent_size = "2",
              },
            },
          },
        },
      })

      lspconfig.ts_ls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        settings = {
          typescript = {
            inlayHints = {
              includeInlayParameterNameHints = "all",
              includeInlayParameterNameHintsWhenArgumentMatchesName = false,
              includeInlayFunctionParameterTypeHints = true,
              includeInlayVariableTypeHints = true,
              includeInlayPropertyDeclarationTypeHints = true,
              includeInlayFunctionLikeReturnTypeHints = true,
              includeInlayEnumMemberValueHints = true,
            },
          },
          javascript = {
            inlayHints = {
              includeInlayParameterNameHints = "all",
              includeInlayParameterNameHintsWhenArgumentMatchesName = false,
              includeInlayFunctionParameterTypeHints = true,
              includeInlayVariableTypeHints = true,
              includeInlayPropertyDeclarationTypeHints = true,
              includeInlayFunctionLikeReturnTypeHints = true,
              includeInlayEnumMemberValueHints = true,
            },
          },
        },
      })

      lspconfig.html.setup({
        capabilities = capabilities,
        on_attach = on_attach,
      })

      lspconfig.cssls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
      })

      lspconfig.eslint.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        settings = {
          codeAction = {
            disableRuleComment = {
              enable = true,
              location = "separateLine",
            },
            showDocumentation = {
              enable = true,
            },
          },
          codeActionOnSave = {
            enable = false,
            mode = "all",
          },
          experimental = {
            useFlatConfig = false,
          },
          format = true,
          nodePath = "",
          onIgnoredFiles = "off",
          packageManager = "npm",
          problems = {
            shortenToSingleLine = false,
          },
          quiet = false,
          rulesCustomizations = {},
          run = "onType",
          useESLintClass = false,
          validate = "on",
          workingDirectory = {
            mode = "location",
          },
        },
      })

      lspconfig.jsonls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        settings = {
          json = {
            schemas = require("schemastore").json.schemas(),
            validate = { enable = true },
          },
        },
      })

      lspconfig.jdtls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        settings = {
          java = {
            signatureHelp = { enabled = true },
            completion = { enabled = true },
            sources = {
              organizeImports = { starThreshold = 9999, staticStarThreshold = 9999 },
            },
          },
        },
      })

      lspconfig.pylsp.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        settings = {
          pylsp = {
            plugins = {
              pycodestyle = { enabled = false },
              mccabe = { enabled = false },
              pyflakes = { enabled = true },
              pylint = { enabled = false },
              autopep8 = { enabled = false },
              yapf = { enabled = false },
              black = { enabled = true },
              isort = { enabled = true },
            },
          },
        },
      })

      lspconfig.bashls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
      })

      vim.diagnostic.config({
        virtual_text = {
          enabled = true,
          source = "if_many",
          prefix = "◆",
        },
        float = {
          source = "always",
          border = "rounded",
          header = "",
          prefix = "",
        },
        signs = {
          text = {
            [vim.diagnostic.severity.ERROR] = "✘",
            [vim.diagnostic.severity.WARN] = "▲",
            [vim.diagnostic.severity.HINT] = "➤",
            [vim.diagnostic.severity.INFO] = "ℹ",
          },
        },
        underline = true,
        update_in_insert = false,
        severity_sort = true,
      })

      vim.lsp.handlers["textDocument/hover"] = vim.lsp.with(vim.lsp.handlers.hover, {
        border = "rounded",
      })

      vim.lsp.handlers["textDocument/signatureHelp"] = vim.lsp.with(vim.lsp.handlers.signature_help, {
        border = "rounded",
      })
    end,
  },

  {
    "akinsho/toggleterm.nvim",
    version = "*",
    config = function()
      require("toggleterm").setup({
        size = function(term)
          if term.direction == "horizontal" then
            return 15
          elseif term.direction == "vertical" then
            return vim.o.columns * 0.4
          end
        end,
        open_mapping = [[<c-\>]],
        hide_numbers = true,
        shade_terminals = true,
        shading_factor = 3,
        start_in_insert = true,
        insert_mappings = true,
        terminal_mappings = true,
        persist_size = true,
        persist_mode = true,
        direction = "float",
        close_on_exit = true,
        shell = vim.o.shell,
        auto_scroll = true,
        float_opts = {
          border = "curved",
          winblend = 10,
          highlights = {
            border = "Normal",
            background = "Normal",
          },
          width = function()
            return math.floor(vim.o.columns * 0.85)
          end,
          height = function()
            return math.floor(vim.o.lines * 0.85)
          end,
        },
        winbar = {
          enabled = false,
        },
        on_create = function()
          vim.opt.foldcolumn = "0"
          vim.opt.signcolumn = "no"
        end,
      })

      function _G.set_terminal_keymaps()
        local opts = { buffer = 0 }
        vim.keymap.set("t", "<esc>", [[<C-\><C-n>]], opts)
        vim.keymap.set("t", "jk", [[<C-\><C-n>]], opts)
        vim.keymap.set("t", "<C-h>", [[<Cmd>wincmd h<CR>]], opts)
        vim.keymap.set("t", "<C-j>", [[<Cmd>wincmd j<CR>]], opts)
        vim.keymap.set("t", "<C-k>", [[<Cmd>wincmd k<CR>]], opts)
        vim.keymap.set("t", "<C-l>", [[<Cmd>wincmd l<CR>]], opts)
        vim.keymap.set("t", "<C-w>", [[<C-\><C-n><C-w>]], opts)
      end

      vim.cmd("autocmd! TermOpen term://* lua set_terminal_keymaps()")
    end,
  },

  {
    "lewis6991/gitsigns.nvim",
    config = function()
      require("gitsigns").setup({
        signs = {
          add = { text = "𓆩▍𓆪" },
          change = { text = "𓆩▍𓆪" },
          delete = { text = "𓆩🗑𓆪" },
          topdelete = { text = "𓆩🗑𓆪" },
          changedelete = { text = "𓆩▍𓆪" },
          untracked = { text = "𓆩▍𓆪" },
        },
        signs_staged = {
          add = { text = "𓆩▍𓆪" },
          change = { text = "𓆩▍𓆪" },
          delete = { text = "𓆩🗑𓆪" },
          topdelete = { text = "𓆩🗑𓆪" },
          changedelete = { text = "𓆩▍𓆪" },
        },
        signs_staged_enable = true,
        signcolumn = true,
        numhl = false,
        linehl = false,
        word_diff = false,
        watch_gitdir = {
          follow_files = true,
        },
        auto_attach = true,
        attach_to_untracked = false,
        current_line_blame = false,
        current_line_blame_opts = {
          virt_text = true,
          virt_text_pos = "eol",
          delay = 800,
          ignore_whitespace = false,
          virt_text_priority = 100,
        },
        current_line_blame_formatter = '<author>, <author_time:%Y-%m-%d> - <summary>',
        sign_priority = 6,
        update_debounce = 100,
        status_formatter = nil,
        max_file_length = 40000,
        preview_config = {
          border = "rounded",
          style = "minimal",
          relative = "cursor",
          row = 0,
          col = 1,
        },
        on_attach = function(bufnr)
          local gitsigns = require("gitsigns")

          local function map(mode, l, r, opts)
            opts = opts or {}
            opts.buffer = bufnr
            vim.keymap.set(mode, l, r, opts)
          end

          map("n", "]c", function()
            if vim.wo.diff then
              vim.cmd.normal({ "]c", bang = true })
            else
              gitsigns.nav_hunk("next")
            end
          end)

          map("n", "[c", function()
            if vim.wo.diff then
              vim.cmd.normal({ "[c", bang = true })
            else
              gitsigns.nav_hunk("prev")
            end
          end)

          map("n", "<leader>hs", gitsigns.stage_hunk)
          map("n", "<leader>hr", gitsigns.reset_hunk)
          map("v", "<leader>hs", function()
            gitsigns.stage_hunk({ vim.fn.line("."), vim.fn.line("v") })
          end)
          map("v", "<leader>hr", function()
            gitsigns.reset_hunk({ vim.fn.line("."), vim.fn.line("v") })
          end)
          map("n", "<leader>hS", gitsigns.stage_buffer)
          map("n", "<leader>hu", gitsigns.undo_stage_hunk)
          map("n", "<leader>hR", gitsigns.reset_buffer)
          map("n", "<leader>hp", gitsigns.preview_hunk)
          map("n", "<leader>hb", function()
            gitsigns.blame_line({ full = true })
          end)
          map("n", "<leader>tb", gitsigns.toggle_current_line_blame)
          map("n", "<leader>hd", gitsigns.diffthis)
          map("n", "<leader>hD", function()
            gitsigns.diffthis("~")
          end)
          map("n", "<leader>td", gitsigns.toggle_deleted)

          map({ "o", "x" }, "ih", ":<C-U>Gitsigns select_hunk<CR>")
        end,
      })
    end,
  },

  {
    "lukas-reineke/indent-blankline.nvim",
    main = "ibl",
    opts = {},
    config = function()
      local highlight = {
        "GothicRed",
        "GothicYellow",
        "GothicBlue",
        "GothicOrange",
        "GothicGreen",
        "GothicViolet",
        "GothicCyan",
      }

      local hooks = require("ibl.hooks")
      hooks.register(hooks.type.HIGHLIGHT_SETUP, function()
        vim.api.nvim_set_hl(0, "GothicRed", { fg = "#e07080" })
        vim.api.nvim_set_hl(0, "GothicYellow", { fg = "#e0c080" })
        vim.api.nvim_set_hl(0, "GothicBlue", { fg = "#7a7af5" })
        vim.api.nvim_set_hl(0, "GothicOrange", { fg = "#e8a070" })
        vim.api.nvim_set_hl(0, "GothicGreen", { fg = "#90c090" })
        vim.api.nvim_set_hl(0, "GothicViolet", { fg = "#b090d8" })
        vim.api.nvim_set_hl(0, "GothicCyan", { fg = "#80c0b8" })
      end)

      require("ibl").setup({
        indent = {
          highlight = highlight,
          char = "│",
        },
        whitespace = {
          highlight = highlight,
          remove_blankline_trail = false,
        },
        scope = {
          enabled = true,
          show_start = true,
          show_end = false,
          injected_languages = false,
          highlight = { "Function", "Label" },
          priority = 500,
        },
      })

      hooks.register(hooks.type.SCOPE_HIGHLIGHT, hooks.builtin.scope_highlight_from_extmark)
    end,
  },

  {
    "windwp/nvim-autopairs",
    event = "InsertEnter",
    config = function()
      require("nvim-autopairs").setup({
        check_ts = true,
        ts_config = {
          lua = { "string", "source" },
          javascript = { "string", "template_string" },
          java = false,
        },
        disable_filetype = { "TelescopePrompt" },
        fast_wrap = {
          map = "<M-e>",
          chars = { "{", "[", "(", '"', "'" },
          pattern = [=[[%'%"%)%>%]%)%}%,]]=],
          offset = 0,
          end_key = ",",
          keys = "qwertyuiopzxcvbnmasdfghjkl",
          check_comma = true,
          highlight = "PmenuSel",
          highlight_grey = "LineNr",
        },
      })

      local cmp_autopairs = require("nvim-autopairs.completion.cmp")
      local cmp = require("cmp")
      cmp.event:on("confirm_done", cmp_autopairs.on_confirm_done())
    end,
  },

  {
    "numToStr/Comment.nvim",
    opts = {},
    config = function()
      require("Comment").setup({
        padding = true,
        sticky = true,
        ignore = nil,
        toggler = {
          line = "gcc",
          block = "gbc",
        },
        opleader = {
          line = "gc",
          block = "gb",
        },
        extra = {
          above = "gcO",
          below = "gco",
          eol = "gcA",
        },
        mappings = {
          basic = true,
          extra = true,
        },
        pre_hook = nil,
        post_hook = nil,
      })
    end,
  },

  {
    "folke/which-key.nvim",
    event = "VeryLazy",
    init = function()
      vim.o.timeout = true
      vim.o.timeoutlen = 300
    end,
    opts = {},
    config = function()
      local wk = require("which-key")
      wk.setup({
        plugins = {
          marks = true,
          registers = true,
          spelling = {
            enabled = true,
            suggestions = 20,
          },
          presets = {
            operators = false,
            motions = true,
            text_objects = true,
            windows = true,
            nav = true,
            z = true,
            g = true,
          },
        },
        operators = { gc = "Comments" },
        key_labels = {},
        motions = {
          count = true,
        },
        icons = {
          breadcrumb = "»",
          separator = "➤",
          group = "◆",
        },
        popup_mappings = {
          scroll_down = "<c-d>",
          scroll_up = "<c-u>",
        },
        window = {
          border = "rounded",
          position = "bottom",
          margin = { 1, 0, 1, 0 },
          padding = { 1, 2, 1, 2 },
          winblend = 10,
          zindex = 1000,
        },
        layout = {
          height = { min = 4, max = 25 },
          width = { min = 20, max = 50 },
          spacing = 3,
          align = "left",
        },
        ignore_missing = true,
        hidden = { "<silent>", "<cmd>", "<Cmd>", "<CR>", "^:", "^ ", "^call ", "^lua " },
        show_help = true,
        show_keys = true,
        triggers = "auto",
        triggers_nowait = {
          "`",
          "'",
          "g`",
          "g'",
          '"',
          "<c-r>",
          "z=",
        },
        triggers_blacklist = {
          i = { "j", "k" },
          v = { "j", "k" },
        },
        disable = {
          buftypes = {},
          filetypes = {},
        },
      })

      wk.register({
        f = {
          name = "file",
          f = { "<cmd>Telescope find_files<cr>", "Find File" },
          g = { "<cmd>Telescope live_grep<cr>", "Live Grep" },
          b = { "<cmd>Telescope buffers<cr>", "Buffers" },
          r = { "<cmd>Telescope oldfiles<cr>", "Open Recent File" },
          n = { "<cmd>enew<cr>", "New File" },
        },
        e = { "<cmd>NvimTreeToggle<cr>", "Explorer" },
        w = { "<cmd>w!<CR>", "Save" },
        q = { "<cmd>q!<CR>", "Quit" },
        c = { "<cmd>bdelete!<CR>", "Close Buffer" },
        t = { "<cmd>ToggleTerm<cr>", "Terminal" },
        h = { name = "Git" },
        l = {
          name = "LSP",
          a = { "<cmd>lua vim.lsp.buf.code_action()<cr>", "Code Action" },
          d = { "<cmd>Telescope diagnostics bufnr=0<cr>", "Document Diagnostics" },
          w = { "<cmd>Telescope diagnostics<cr>", "Workspace Diagnostics" },
          f = { "<cmd>lua vim.lsp.buf.format{async=true}<cr>", "Format" },
          i = { "<cmd>LspInfo<cr>", "Info" },
          I = { "<cmd>LspInstallInfo<cr>", "Installer Info" },
          j = { "<cmd>lua vim.lsp.diagnostic.goto_next()<CR>", "Next Diagnostic" },
          k = { "<cmd>lua vim.lsp.diagnostic.goto_prev()<cr>", "Prev Diagnostic" },
          l = { "<cmd>lua vim.lsp.codelens.run()<cr>", "CodeLens Action" },
          q = { "<cmd>lua vim.lsp.diagnostic.set_loclist()<cr>", "Quickfix" },
          r = { "<cmd>lua vim.lsp.buf.rename()<cr>", "Rename" },
          s = { "<cmd>Telescope lsp_document_symbols<cr>", "Document Symbols" },
          S = { "<cmd>Telescope lsp_dynamic_workspace_symbols<cr>", "Workspace Symbols" },
        },
        g = {
          name = "Git",
          g = { "<cmd>lua _LAZYGIT_TOGGLE()<CR>", "Lazygit" },
          j = { "<cmd>lua require 'gitsigns'.next_hunk()<cr>", "Next Hunk" },
          k = { "<cmd>lua require 'gitsigns'.prev_hunk()<cr>", "Prev Hunk" },
          l = { "<cmd>lua require 'gitsigns'.blame_line()<cr>", "Blame" },
          p = { "<cmd>lua require 'gitsigns'.preview_hunk()<cr>", "Preview Hunk" },
          r = { "<cmd>lua require 'gitsigns'.reset_hunk()<cr>", "Reset Hunk" },
          R = { "<cmd>lua require 'gitsigns'.reset_buffer()<cr>", "Reset Buffer" },
          s = { "<cmd>lua require 'gitsigns'.stage_hunk()<cr>", "Stage Hunk" },
          u = { "<cmd>lua require 'gitsigns'.undo_stage_hunk()<cr>", "Undo Stage Hunk" },
          o = { "<cmd>Telescope git_status<cr>", "Open changed file" },
          b = { "<cmd>Telescope git_branches<cr>", "Checkout branch" },
          c = { "<cmd>Telescope git_commits<cr>", "Checkout commit" },
          d = { "<cmd>Gitsigns diffthis HEAD<cr>", "Diff" },
        },
      }, { prefix = "<leader>" })
    end,
  },

  {
    "rcarriga/nvim-notify",
    config = function()
      require("notify").setup({
        background_colour = "#0e0e15",
        fps = 60,
        icons = {
          DEBUG = "𓆩🐞𓆪",
          ERROR = "𓆩✘𓆪",
          INFO = "𓆩ℹ𓆪",
          TRACE = "𓆩✎𓆪",
          WARN = "𓆩▲𓆪",
        },
        level = 2,
        minimum_width = 50,
        render = "compact",
        stages = "fade",
        time_formats = {
          notification = "%T",
          notification_history = "%FT%T",
        },
        timeout = 3000,
        top_down = false,
      })
      vim.notify = require("notify")
    end,
  },

  {
    "folke/noice.nvim",
    event = "VeryLazy",
    dependencies = {
      "MunifTanjim/nui.nvim",
      "rcarriga/nvim-notify",
    },
    config = function()
      require("noice").setup({
        lsp = {
          override = {
            ["vim.lsp.util.convert_input_to_markdown_lines"] = true,
            ["vim.lsp.util.stylize_markdown"] = true,
            ["cmp.entry.get_documentation"] = true,
          },
        },
        presets = {
          bottom_search = true,
          command_palette = true,
          long_message_to_split = true,
          inc_rename = false,
          lsp_doc_border = true,
        },
        messages = {
          enabled = true,
          view = "notify",
          view_error = "notify",
          view_warn = "notify",
          view_history = "messages",
          view_search = "virtualtext",
        },
        cmdline = {
          enabled = true,
          view = "cmdline_popup",
          opts = {},
          format = {
            cmdline = { pattern = "^:", icon = "❯", lang = "vim" },
            search_down = { kind = "search", pattern = "^/", icon = "𓆩🔍𓆪", lang = "regex" },
            search_up = { kind = "search", pattern = "^%?", icon = "𓆩🔍𓆪", lang = "regex" },
            filter = { pattern = "^:%s*!", icon = ">", lang = "bash" },
            lua = { pattern = "^:%s*lua%s+", icon = "🌙", lang = "lua" },
            help = { pattern = "^:%s*he?l?p?%s+", icon = "❓" },
            input = {},
          },
        },
        popupmenu = {
          enabled = true,
          backend = "nui",
          kind_icons = {},
        },
        redirect = {
          view = "popup",
          filter = { event = "msg_show" },
        },
        commands = {
          history = {
            view = "split",
            opts = { enter = true, format = "details" },
            filter = {
              any = {
                { event = "notify" },
                { error = true },
                { warning = true },
                { event = "msg_show", kind = { "" } },
                { event = "lsp", kind = "message" },
              },
            },
          },
          last = {
            view = "popup",
            opts = { enter = true, format = "details" },
            filter = {
              any = {
                { event = "notify" },
                { error = true },
                { warning = true },
                { event = "msg_show", kind = { "" } },
                { event = "lsp", kind = "message" },
              },
            },
            filter_opts = { count = 1 },
          },
          errors = {
            view = "popup",
            opts = { enter = true, format = "details" },
            filter = { error = true },
            filter_opts = { reverse = true },
          },
        },
        notify = {
          enabled = true,
          view = "notify",
        },
        health = {
          checker = true,
        },
      })
    end,
  },

  {
    "b0o/schemastore.nvim",
  },
})

local function map(mode, lhs, rhs, opts)
  local options = { noremap = true, silent = true }
  if opts then
    options = vim.tbl_extend("force", options, opts)
  end
  vim.keymap.set(mode, lhs, rhs, options)
end

map("n", "<leader>e", "<cmd>NvimTreeToggle<CR>")
map("n", "<leader>ff", "<cmd>Telescope find_files<CR>")
map("n", "<leader>fg", "<cmd>Telescope live_grep<CR>")
map("n", "<leader>fb", "<cmd>Telescope buffers<CR>")
map("n", "<leader>fh", "<cmd>Telescope help_tags<CR>")
map("n", "<leader>fo", "<cmd>Telescope oldfiles<CR>")
map("n", "<Tab>", "<cmd>BufferLineCycleNext<CR>")
map("n", "<S-Tab>", "<cmd>BufferLineCyclePrev<CR>")
map("n", "<leader>c", "<cmd>bdelete<CR>")
map("n", "<leader>bc", "<cmd>BufferLinePickClose<CR>")
map("n", "<leader>bp", "<cmd>BufferLinePick<CR>")
map("n", "<leader>t", "<cmd>ToggleTerm<CR>")
map("n", "<C-h>", "<C-w>h")
map("n", "<C-j>", "<C-w>j")
map("n", "<C-k>", "<C-w>k")
map("n", "<C-l>", "<C-w>l")
map("n", "<leader>w", "<cmd>w<CR>")
map("n", "<leader>q", "<cmd>q<CR>")
map("n", "<leader>x", "<cmd>qa<CR>")
map("n", "<Esc>", "<cmd>nohlsearch<CR>")

map("v", "<", "<gv")
map("v", ">", ">gv")
map("v", "<A-j>", ":m .+1<CR>==")
map("v", "<A-k>", ":m .-2<CR>==")
map("v", "p", '"_dP')

map("x", "J", ":move '>+1<CR>gv-gv")
map("x", "K", ":move '<-2<CR>gv-gv")
map("x", "<A-j>", ":move '>+1<CR>gv-gv")
map("x", "<A-k>", ":move '<-2<CR>gv-gv")

map("n", "<A-j>", "<Esc>:m .+1<CR>==gi")
map("n", "<A-k>", "<Esc>:m .-2<CR>==gi")

map("n", "<C-Up>", ":resize +2<CR>")
map("n", "<C-Down>", ":resize -2<CR>")
map("n", "<C-Left>", ":vertical resize -2<CR>")
map("n", "<C-Right>", ":vertical resize +2<CR>")

map("i", "jk", "<ESC>")
map("i", "kj", "<ESC>")

map("n", "n", "nzzzv")
map("n", "N", "Nzzzv")

map("n", "J", "mzJ`z")

map("n", "<C-d>", "<C-d>zz")
map("n", "<C-u>", "<C-u>zz")

vim.api.nvim_create_autocmd("TextYankPost", {
  desc = "Highlight when yanking (copying) text",
  group = vim.api.nvim_create_augroup("kickstart-highlight-yank", { clear = true }),
  callback = function()
    vim.highlight.on_yank({ higroup = "Visual", timeout = 200 })
  end,
})

vim.api.nvim_create_autocmd("FileType", {
  pattern = "NvimTree",
  callback = function()
    vim.opt_local.winhl = "Normal:NvimTreeNormal,EndOfBuffer:NvimTreeEndOfBuffer"
  end,
})

vim.api.nvim_create_autocmd("BufEnter", {
  pattern = "*",
  callback = function()
    vim.opt.formatoptions:remove({ "c", "r", "o" })
  end,
})

vim.api.nvim_create_autocmd("VimResized", {
  callback = function()
    vim.cmd("tabdo wincmd =")
  end,
})
