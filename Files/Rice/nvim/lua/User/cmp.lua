-- http://neovimcraft.com/plugin/hrsh7th/nvim-cmp/index.html
local cmpStatusOk, cmp = pcall(require, "cmp")
if not cmpStatusOk then
    return
end

local snipStatusOk, luasnip = pcall(require, "luasnip")
if not snipStatusOk then
    return
end

require("luasnip/loaders/from_vscode").lazy_load()

local checkBackspace = function()
    local col = vim.fn.col "." - 1
    return col == 0 or vim.fn.getline("."):sub(col, col):match "%s"
end

-- Source: https://www.nerdfonts.com/cheat-sheet
--   פּ ﯟ   some other good icons
local kind_icons = {
    Text = "󰉿",
	Method = "󰆧",
	Function = "󰊕",
	Constructor = "",
    Field = " ",
	Variable = "󰀫",
	Class = "󰠱",
	Interface = "",
	Module = "",
	Property = "󰜢",
	Unit = "󰑭",
	Value = "󰎠",
	Enum = "",
	Keyword = "󰌋",
    Snippet = "",
	Color = "󰏘",
	File = "󰈙",
    Reference = "",
	Folder = "󰉋",
	EnumMember = "",
	Constant = "󰏿",
    Struct = "",
	Event = "",
	Operator = "󰆕",
    TypeParameter = " ",
	Misc = " ",
}

-- ctrl + space open menu
-- ctlr + e     close menu

cmp.setup {
    snippet = {
        expand = function(args)
          luasnip.lsp_expand(args.body) -- For `luasnip` users.
        end,
    },
    mapping = {
    ["<C-k>"] = cmp.mapping.select_prev_item(),
    ["<C-j>"] = cmp.mapping.select_next_item(),
    ["<C-b>"] = cmp.mapping(cmp.mapping.scroll_docs(-1), { "i", "c" }),
    ["<C-f>"] = cmp.mapping(cmp.mapping.scroll_docs(1), { "i", "c" }),
    ["<C-Space>"] = cmp.mapping(cmp.mapping.complete(), { "i", "c" }),
    ["<C-y>"] = cmp.config.disable, -- Specify `cmp.config.disable` if you want to remove the default `<C-y>` mapping.
    ["<C-e>"] = cmp.mapping {
      i = cmp.mapping.abort(),
      c = cmp.mapping.close(),
    },
    -- Accept currently selected item. If none selected, `select` first item.
    -- Set `select` to `false` to only confirm explicitly selected items.
    ["<CR>"] = cmp.mapping.confirm { select = true },

    -- Super tab
    ["<Tab>"] = cmp.mapping(function(fallback)
        if cmp.visible() then
        cmp.select_next_item()
        elseif luasnip.expandable() then
        luasnip.expand()
        elseif luasnip.expand_or_jumpable() then
        luasnip.expand_or_jump()
        elseif checkBackspace() then
        fallback()
        else
        fallback()
        end
        end, {
        "i",
        "s",
    }),
    ["<S-Tab>"] = cmp.mapping(function(fallback)
        if cmp.visible() then
        cmp.select_prev_item()
        elseif luasnip.jumpable(-1) then
        luasnip.jump(-1)
        else
        fallback()
        end
        end, {
        "i",
        "s",
        }),
    },

    -- Setting for formatting
    formatting = {
        fields = { "kind", "abbr", "menu" },
        format = function(entry, vim_item)
            -- Kind icons
            vim_item.kind = string.format("%s", kind_icons[vim_item.kind])
            -- -- vim_item.kind = string.format('%s %s', kind_icons[vim_item.kind], vim_item.kind) -- This concatonates the icons with the name of the item kind
      
            vim_item.menu = ({
                nvim_lsp = "[LSP]",
                -- luasnip = "[Snippet]",
                buffer = "[Buffer]",
                path = "[Path]",
            })[entry.source.name]
            -- https://github.com/hrsh7th/nvim-cmp/issues/88#issuecomment-906585635
            vim_item.abbr = string.sub(vim_item.abbr, 1, vim.api.nvim_win_get_width(0) / 2)
            return vim_item
        end,
    },
    sources = {
        { name = "nvim_lsp" },
        -- { name = "luasnip" },
        { name = "buffer" },
        { name = "path" },
        },
        confirm_opts = {
            behavior = cmp.ConfirmBehavior.Replace,
            select = false,
        },
        window = {
            documentation = cmp.config.window.bordered(),
        },
        experimental = {
            ghost_text = false,
            native_menu = false,
    },

    -- Set configuration for specific filetype.
    -- Set configuration for text files.
    cmp.setup.filetype('text', {
    sources = cmp.config.sources({
      {}, -- You can specify the `cmp_git` source if you were installed it.
    }, {
      {},
    })
    })
}
